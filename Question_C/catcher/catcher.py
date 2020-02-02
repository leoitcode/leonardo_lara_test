
import requests

from nameko.rpc import rpc
from redis import Redis
from urllib.parse import quote_plus
from googlesearch import search

import time


class Catcher:
    name = 'serv_catcher'

    redis = Redis(host='localhost', port=6379, db=0)

    @rpc
    def get_links(self,n_search):

        search_str = self.redis.get('string')

        #Transform the string into a URL Standard
        search_str = quote_plus(search_str)

        count=1

        #Generates links from google
        for url in search(search_str,stop=n_search):


            #Send the link to Redis DB with link1, link2.. keys
            lnk_n = str(count)
            self.redis.set("link"+lnk_n,url)

            count+=1
            print(f"Link {url} has got with success!")

            #Time to avoid be blocked by Google
            time.sleep(2)


        return