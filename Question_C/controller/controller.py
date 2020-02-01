import json
import random

from nameko.rpc import RpcProxy,rpc


class Controller:
    name = 'serv_controller'

    catcher = RpcProxy('serv_catcher')
    crawler = RpcProxy('serv_crawler')
    interpreter = RpcProxy('serv_interpreter')


    @rpc
    def controller(self,query):

        self.catcher.get_links.call_async()

        self.crawler.get_crawls.call_async()

        self.interpreter.get_insights.call_async()








