import json
import random

from nameko.rpc import RpcProxy,rpc
from nameko.web.handlers import http
from collections import deque
from datetime import datetime as dtt, timedelta



class OmurcoServer:
    name = 'server'

    can_cli = RpcProxy('canada_client')
    usa_cli = RpcProxy('usa_client')
    bra_cli = RpcProxy('brazil_client')

    cache_server = deque(['PYTHON','JAVA','JAVA_SCRIPT','PHP'])
    cache_time = dtt.now()

    cache_size = 7


    @http('GET', '/cache/<string:client_id>/<string:code>')
    def get_cache(self, request, client_id, code):

        if code not in self.cache_server:

            strp_cli = client_id.strip().lower()

            if ('canada' in strp_cli):
                cache = self.can_cli.get_cache(code)
            elif ('usa' in strp_cli) or ('united' in strp_cli):
                cache = self.usa_cli.get_cache(code)
            elif('brazil' in strp_cli):
                cache = self.bra_cli.get_cache(code)
            elif('server' in strp_cli):
                cache = self.cache_server

            self.check_expire()

            if code in cache:

                return json.dumps({'cache': list(cache)})

            else:

                return "I don't have this programming language in cache."


        else:

            return json.dumps({'cache': list(self.cache_server)})


    @http('POST', '/post/<string:client_aim>')
    def do_post(self, request,client_aim):

        cod = request.get_data(as_text=True)

        if client_aim == 'canada':
            res = self.can_cli.add_cache(cod)
            print('Cached on '+client_aim)

        elif client_aim == 'usa':
            res = self.usa_cli.add_cache(cod)
            print('Cached on '+client_aim)

        elif client_aim == 'brazil':
            res = self.bra_cli.add_cache(cod)
            print('Cached on '+client_aim)
            
        elif client_aim == 'server':
            res = self.add_cache(cod)
            print('Cached on '+client_aim)

        self.check_expire()        

        return u"received: {}".format(cod)


    def add_cache(self,code):

        if code not in self.cache_server:

            if len(self.cache_server) < self.cache_size:

                self.cache_server.append(code)

            else:
                self.cache_server.pop()
                self.cache_server.append(code)

        else:

            return 'I already have this data on cache.'


    def expire_cache(self):

        if (self.cache_time+timedelta(minutes=30)) < dtt.now():

            self.cache_server.pop()
            self.cache_time = dtt.now()


    def check_expire(self):

        self.expire_cache()
        self.can_cli.expire_cache()
        self.usa_cli.expire_cache()
        self.bra_cli.expire_cache()
