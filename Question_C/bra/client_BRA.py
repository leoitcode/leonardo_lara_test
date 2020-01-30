import json

from nameko.rpc import rpc
from collections import deque
from datetime import datetime as dtt, timedelta


class BrazilClient:
    name = 'brazil_client'

    cache_bra = deque(['LUA'])
    cache_bra_time = dtt.now()

    cache_size = 7


    @rpc
    def get_cache(self, code):

        return list(self.cache_bra)

    @rpc
    def add_cache(self, code):

        if code not in self.cache_bra:
            
            if len(self.cache_bra) < self.cache_size:

                self.cache_bra.append(code)

            else:
                self.cache_bra.pop()
                self.cache_bra.append(code)

        else:

           return 'I already have this data on cache.'

    @rpc
    def expire_cache(self):

        if (self.cache_bra_time+timedelta(minutes=30)) < dtt.now():

            self.cache_bra.pop()
            self.cache_bra_time = dtt.now()