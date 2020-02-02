from nameko.rpc import RpcProxy,rpc
from redis import Redis
from loguru import logger as log

import json
import time


class Controller:
    name = 'serv_controller'

    catcher = RpcProxy('serv_catcher')
    crawler = RpcProxy('serv_crawler')

    r = Redis(host='localhost', port=6379, db=0, decode_responses=True)
    
    insights = []
    

    @rpc
    def controller(self,query,n_search):

        log.info("-- STARTING CONTROLLER --")

        self.r.flushdb()

        self.r.delete("string")

        log.info(f"-- Received sentence: {query}")

        self.r.set("string",query)

        log.info("-- STARTING SERVICES --")

        self.catcher.get_links.call_async(n_search)
        
        self.crawler.get_crawls.call_async()

        count=0

        self.insights = []

        while count<n_search:

            if self.r.exists("crawls"):


                ins = self.r.lpop("crawls")

                log.info("Received Crawled page")

                self.insights.append(ins)

                count+=1
                time.sleep(2)


            time.sleep(1)
            log.info("-- WAITING FOR DATA...")

        return self.insights


        








