import json
import random

from nameko.rpc import RpcProxy,rpc


class Controller:
    name = 'serv_controller'

    catcher = RpcProxy('serv_catcher')
    crawler = RpcProxy('serv_crawler')
    interpreter = RpcProxy('serv_interpreter')


    @rpc
    def controller(self):

        





