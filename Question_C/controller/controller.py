
from nameko.rpc import RpcProxy,rpc
from redis import Redis


class Controller:
    name = 'serv_controller'

    catcher = RpcProxy('serv_catcher')
    #crawler = RpcProxy('serv_crawler')
    #interpreter = RpcProxy('serv_interpreter')

    redis = Redis(host='localhost', port=6379, db=0)



    @rpc
    def controller(self,query):

        self.redis.set("string",query)

        self.catcher.get_links.call_async(n_search=5)
        
        self.crawler.get_crawls.call_async()

        #self.interpreter.get_insights.call_async()

        return








