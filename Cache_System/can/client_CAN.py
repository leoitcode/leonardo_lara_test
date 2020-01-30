import json

from nameko.rpc import rpc
from collections import deque
from datetime import datetime as dtt, timedelta


class BrazilClient:
    name = 'canada_client'

    cache_can = deque(['C++'])
    cache_can_time = dtt.now()

    cache_size = 7


    @rpc
    def get_cache(self, code):

        return list(self.cache_can)

    @rpc
    def add_cache(self, code):

        if code not in self.cache_can:
            
            if len(self.cache_can) < self.cache_size:

                self.cache_can.append(code)

            else:
                self.cache_can.pop()
                self.cache_can.append(code)

        else:

           return 'I already have this data on cache.'

    @rpc
    def expire_cache(self):

        if (self.cache_can_time+timedelta(minutes=30)) < dtt.now():

            self.cache_can.pop()
            self.cache_can_time = dtt.now()