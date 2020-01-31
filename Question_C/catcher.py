import json
import random

from nameko.rpc import RpcProxy,rpc
from nameko.web.handlers import http

class catcher:
    name = 'catcher'

    controller = RpcProxy('controler'),

    @http('GET', '/crawler/<string:query>')
    def get_cache(self, request, query):

        if query:

            try:
                self.controller.()



