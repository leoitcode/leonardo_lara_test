import json

from nameko.rpc import rpc
from collections import deque
from datetime import datetime as dtt, timedelta


class CanadaClient:
    name = 'canada_client'

    cache_canada = deque(['C++'])
    cache_canada_time = dtt.now()

    cache_size = 7


    @rpc
    def get_cache(self, code):

                return list(self.cache_canada)


    @rpc
    def add_cache(self, code):

        if code not in self.cache_canada:
            
            if len(self.cache_canada) < self.cache_size:

                self.cache_canada.append(code)

            else:
                self.cache_canada.pop()
                self.cache_canada.append(code)

        else:

                return 'I already have this data on cache.'

    @rpc
    def expire_cache(self):

        if (self.cache_canada_time+timedelta(minutes=30)) < dtt.now():

            self.cache_canada.pop()
            self.cache_canada_time = dtt.now()




