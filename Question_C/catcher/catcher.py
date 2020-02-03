
import requests
import time
import os

from nameko.rpc import rpc
from redis import Redis
from urllib.parse import quote_plus
from googlesearch import search
from loguru import logger as log




class Catcher:
    name = 'serv_catcher'

    ''' Nameko Service serv_catcher for catch links 
        and send in real time to Crawler service

        SET: Put links inside REDIS DataBase to any Crawler Service get
    '''

    R_HOST = os.getenv('REDIS_HOST')
    R_PORT = os.getenv('REDIS_PORT')

    r = Redis(host=R_HOST, port=R_PORT, db=0, decode_responses=True)

    @rpc
    def get_links(self,n_search):


        log.info("-- STARTING CATCHER --")

        #Persist String key with Search Term
        search_str = self.r.get('string')
        self.r.set("string",search_str)

        #Transform the string into a URL Standard
        search_str = quote_plus(search_str)
        print(search_str)

        #Generates links from google
        for url in search(search_str,stop=n_search):

            #Check if the URL already exists in the list
            if self.isOnList(url):
                continue

            #Create a Redis list and put url on Right (rpush)
            self.r.rpush("links",url)
            self.r.rpush("bak_links",url)


            #Send the link to Redis DB with link1, link2.. keys
            log.info(f"-- Link {url} has got with success!")

            #Time to avoid be blocked by Google
            time.sleep(2)

        return 



    def isOnList(self,url):

        ''' This function checks if the URL is repeated.
        '''

        urlb = url.encode()

        #Iterate over link list
        for i in range(0, self.r.llen("links")+1):
            
            #Check if url is on list
            v = self.r.lindex("links", i)

            if v==urlb:
                log.warning(f"-- I already have this URL")
                return True

        return False


