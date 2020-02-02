
from nameko.rpc import RpcProxy,rpc
from redis import Redis


class Controller:
    name = 'serv_controller'

    catcher = RpcProxy('serv_catcher')
    crawler = RpcProxy('serv_crawler')
    #interpreter = RpcProxy('serv_interpreter')

    r = Redis(host='localhost', port=6379, db=0)
    r.flushall()



    @rpc
    def controller(self,query,n_search):

        self.r.set("string",query)

        self.catcher.get_links.call_async(n_search)
        
        self.crawler.get_crawls.call_async()

        r.rpush("crawls",result)

        








