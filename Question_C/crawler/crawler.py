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


class Crawler:
    name = 'serv_crawler'

    r = Redis(host='localhost', port=6379, db=0, decode_responses=True)

    soup = None
    pattern = None

    @rpc
    def get_crawls(self):

        log.info("-- STATING CRAWLER --")

        while True:

            if self.r.exists("links"):

                time.sleep(1)

                link = self.r.lpop("links")

                if not link:
                    continue

                self.crawl_page(link)
                time.sleep(1)


            log.info("Waiting for Links...")
            time.sleep(1)




    def crawl_page(self,link):

        search_str = self.r.get('string')

        useless_words = set(stopwords.words('english'))

        tsearch_str = word_tokenize(str(search_str))

        words = [s for s in tsearch_str if not s in useless_words]

        self.pattern = r"(" + "|".join(words) + ")"

        log.debug(f"Querying page: {link}")

        response = requests.get(link)

        if not response:
            log.warning(f"Was impossible to get from link: {link}")
            return

        self.soup = bs(response.text, "html.parser")

        tags_del = ['header','meta','script','style']

        for x in self.soup(tags_del):
            x.extract()
            

        text = self.extract_text(['p','span','q'])

        title = self.extract_text(['title'])

        subtitles = self.extract_text(['h'+str(i) for i in range(1,7)])

        code = self.extract_text(['code'])

        lists = self.extract_text(['li'])


        initial_links = self.r.lrange("bak_links", 0, -1 )

        result = {'links':initial_links,'sentence':search_str,'text':text,'title':title,'subtitles':subtitles,'code':code,'lists':lists}

        result = json.dumps(result)

        result = result.replace('\\"','"')
        result = result.replace('\\\"','\\')

        self.r.rpush("crawls",result)



    def extract_text(self,*tags,trig=True):

        txts=None
        
        for tag in tags:
            
            if trig:
                txts = self.soup.findAll(tag, text = re.compile(self.pattern,re.IGNORECASE))
                trig=False
                continue
                
            txts+=self.soup.findAll(tag, text = re.compile(self.pattern,re.IGNORECASE))
        
        
        _tmp = []
        
        for txt in txts:
            _tmp.append(txt.get_text())
        
        return _tmp
