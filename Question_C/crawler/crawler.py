from nameko.rpc import rpc
from redis import Redis
from bs4 import BeautifulSoup as bs
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

import time
import requests
import json


class Crawler:
    name = 'serv_crawler'

    r = Redis(host='localhost', port=6379, db=0)

    search_str = self.r.get('string')

    @rpc
    def get_crawls(self):

        while True:

            if r.llen("links")!=0:

                link = r.lpop("links")
                self.crawl_page(link)



    def crawl_page(self,link):


        useless_words = set(stopwords.words('english'))

        search_str = word_tokenize(self.search_str)

        words = [s for s in search_str if not s in useless_words]

        pattern = r"(" + "|".join(words) + ")"

        html_page = requests.get(link)

        soup = bs(html_page.content)

        tags_del = ['header','meta','head','script','style']

        for x in soup(tags_del):
            x.extract()
            

        text = self.extract_text(['p','span','q'])

        title = self.extract_text(['title'])

        subtitles = self.extract_text(['h'+str(i) for i in range(1,7)])

        code = self.extract_text(['code'])

        lists = self.extract_text(['li'])

        result = {'text':text,'title':title,'subtitles':subtitles,'code':code,'lists':lists}

        result = json.dumps(result)

        r.rpush("crawls",result)



    def extract_text(*tags,trig=True):

        txts=None
        
        for tag in tags:
            
            if trig:
                txts = soup.findAll(tag, text = re.compile(pattern,re.IGNORECASE))
                trig=False
                continue
                
            txts+=soup.findAll(tag, text = re.compile(pattern,re.IGNORECASE))
        
        
        _tmp = []
        
        for txt in txts:
            _tmp.append(txt.get_text())
        
        return _tmp
