import json

from nameko.rpc import rpc
from collections import deque
from datetime import datetime as dtt, timedelta


class USAClient:
    name = 'usa_client'

    cache_usa = deque(['FORTRAN'])
    cache_usa_time = dtt.now()

    cache_size = 7


    @rpc
    def get_cache(self, code):

        return list(self.cache_usa)


    @rpc
    def add_cache(self, code):

        if code not in self.cache_usa:

            if len(self.cache_usa) < self.cache_size:

                self.cache_usa.append(code)

            else:
                self.cache_usa.pop()
                self.cache_usa.append(code)

        else:

            return 'I already have this data on cache.'

    @rpc
    def expire_cache(self):

        if (self.cache_usa_time+timedelta(minutes=30)) < dtt.now():

            self.cache_usa.pop()
            self.cache_usa_time = dtt.now()