from nameko.rpc import RpcProxy,rpc
from redis import Redis
from loguru import logger as log

import json
import time
import os


class Controller:
    name = 'serv_controller'

    ''' Nameko Service serv_controller to control the Catcher and Crawler services.
        Could be more services on to get fast information.

        SET: Start the two services asynchronously.
        OUTPUT: Send to Gateway the crawled pages when the work is finished.
    '''

    catcher = RpcProxy('serv_catcher')
    crawler = RpcProxy('serv_crawler')

    R_HOST = os.getenv('REDIS_HOST')
    R_PORT = os.getenv('REDIS_PORT')

    r = Redis(host=R_HOST, port=R_PORT, db=0, decode_responses=True)
    
    insights = []
    

    @rpc
    def controller(self,query,n_search):

        log.info("-- STARTING CONTROLLER --")


        #Ensure that Redis DataBase is empty
        self.r.flushdb()
        self.r.delete("string")


        log.info(f"-- Received sentence: {query}")

        self.r.set("string",query)

        log.info("-- STARTING SERVICES --")


        #Start the Async Services
        self.catcher.get_links.call_async(n_search)
        self.crawler.get_crawls.call_async()

        count=0

        self.insights = []

        #Check if Crawler sent a Page in "crawls" list
        while count<n_search:

            if self.r.exists("crawls"):


                ins = self.r.lpop("crawls")

                log.info("Received Crawled page")

                if count == 4:
                    self.insights = [ins] + self.insights

                self.insights.append(ins)
                log.info("-- WAITING FOR DATA...")

                count+=1
                time.sleep(2)

            time.sleep(1)
            

        return self.insights


        








