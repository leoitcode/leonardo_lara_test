from nameko.rpc import rpc
from redis import Redis
from bs4 import BeautifulSoup as bs
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from loguru import logger as log

import time
import requests
import json
import re
import os


class Crawler:
    name = 'serv_crawler'

    ''' Nameko Service serv_crawler for crawl pages
        and send back to controller in real time.

    '''

    soup = None
    pattern = None

    R_HOST = os.getenv('REDIS_HOST')
    R_PORT = os.getenv('REDIS_PORT')

    r = Redis(host=R_HOST, port=R_PORT, db=0, decode_responses=True)

    @rpc
    def get_crawls(self):

        ''' Often grabs a link in Redis Database and crawl the page.
            SET: Send a valid link to crawl_page function
        '''

        log.info("-- STATING CRAWLER --")


        #Check if there is a valid link in "LINKS" Redis list
        while True:

            if self.r.exists("links"):

                time.sleep(1)

                #Get left element from list and pop
                link = self.r.lpop("links")

                if not link:
                    continue

                #Call the Crawl_page function on link
                self.crawl_page(link)
                log.info("-- WAITING FOR LINKS --")
                time.sleep(1)
            
            time.sleep(1)




    def crawl_page(self,link):

        ''' Process words, and find tags with specific words.

            SET: Put Strings Json Format (for json.load in client)
                 in Redis DataBase for Controller access in real time.
        '''

        #Get the searched word from Redis Database
        search_str = self.r.get('string')

        #Create a set of STOPWORDS to ignore
        useless_words = set(stopwords.words('english'))

        #Create a set of words
        tsearch_str = word_tokenize(str(search_str))

        #Drop the useless words on set
        words = [s for s in tsearch_str if not s in useless_words]

        #Create a Regex pattern to find words
        self.pattern = r"(" + "|".join(words) + ")"

        log.debug(f"Querying page: {link}")

        response = requests.get(link)

        if not response:
            log.warning(f"Was impossible to get from link: {link}")
            return

        self.soup = bs(response.text, "html.parser")

        #Drop some useless tags for the purpose
        tags_del = ['header','meta','script','style']

        for x in self.soup(tags_del):
            x.extract()


            
        #Use extract_text function to get text, title etc
        text = self.extract_text(['p','span','q'])
        title = self.extract_text(['title'])
        subtitles = self.extract_text(['h'+str(i) for i in range(1,7)])
        code = self.extract_text(['code'])
        lists = self.extract_text(['li'])


        #Initial links from Catcher
        initial_links = self.r.lrange("bak_links", 0, -1)

        #Store all information in result dictionary
        result = {'links':initial_links,'sentence':search_str,'text':text,'title':title,'subtitles':subtitles,'code':code,'lists':lists}

        #Convert a dictionary into string json.
        result = json.dumps(result)
        result = result.replace('\\"','"')
        result = result.replace('\\\"','\\')

        #Store crawled page into Redis Database for Controller
        self.r.rpush("crawls",result)



    def extract_text(self,*tags,trig=True):

        ''' This function extract text based on tag or many tags and Regex pattern
            OUTPUT: List with extractions
        '''

        txts=None
        
        for tag in tags:
            
            if trig:

                #Extract on "tag" text containing the pattern
                txts = self.soup.findAll(tag, text = re.compile(self.pattern,re.IGNORECASE))
                trig=False
                continue
                
            txts+=self.soup.findAll(tag, text = re.compile(self.pattern,re.IGNORECASE))
        
        
        _tmp = []
        
        for txt in txts:
            _tmp.append(txt.get_text())
        
        return _tmp
