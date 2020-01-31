import json
import random

from nameko.rpc import RpcProxy,rpc
from nameko.web.handlers import http

class catcher:
    name = 'serv_catcher'

    controller = RpcProxy('controler'),

    @http('GET', '/crawler/<string:query>')
    def get_cache(self, request, query):

        if query:

            try:
                dicts = self.controller.controller(query)

            except Exception as e:
                print("Couldn't connect to Crawler Service")


            return dicts






