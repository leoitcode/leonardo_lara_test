
import requests

from nameko.rpc import rpc
from redis import Redis
from urllib.parse import quote_plus
from googlesearch import search

import time


class Catcher:
    name = 'serv_catcher'

    r = Redis(host='localhost', port=6379, db=0)

    @rpc
    def get_links(self,n_search):

        search_str = self.r.get('string')

        #Transform the string into a URL Standard
        search_str = quote_plus(search_str)

        #Generates links from google
        for url in search(search_str,stop=n_search):

            if isOnList(url):
                continue

            #Add in Redis "links" list
            r.rpush("links",url)
            r.rpush("bak_links",url)


            #Send the link to Redis DB with link1, link2.. keys
            print(f"Link {url} has got with success!")

            #Time to avoid be blocked by Google
            time.sleep(2)

        return 



    def isOnList(self,url):

        urlb = url.encode()

        for i in range(0, r.llen("links")+1):
    
            v = r.lindex("links", i)

            if v==urlb:
                print("I already have this URL.")
                return True

        return False


