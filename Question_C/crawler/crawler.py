from nameko.rpc import rpc
from redis import Redis

import time


class Crawler:
    name = 'serv_crawler'

    r = Redis(host='localhost', port=6379, db=0)
    del_keys = []

    @rpc
    def get_crawls(self):

        while True:


            for key in self.r.scan_iter(match='link*'):

                link = self.r.get(key)
                self.r.delete(key)

                if key not in self.del_keys:
                    self.crawl_page(link)

                self.del_keys.append(key)
                


        self.r.set("result","Minha resposta")

        return


    def crawl_page(self,page):

        print(page)

        return


