import json
import os

from nameko.standalone.rpc import ClusterRpcProxy
from loguru import logger as log


def start_crawl(query):

    USERNAME = os.getenv('RABBIT_USER')
    PASSWORD = os.getenv('RABBIT_PASSWORD')
    HOST = os.getenv('RABBIT_HOST')
    PORT = os.getenv('RABBIT_PORT')


    config = {"AMQP_URI": f"amqp://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/"}


    #Log Configuration
    log_file_name = '../logs/' + 'today' + '.log'

    log.add(
        log_file_name,
        level="DEBUG",
        backtrace=True,
        diagnose=True,
        rotation="00:00"
        )


    if query:

        log.info("-- STARTING THE CRAWLER --")

        try:    

            #Create a Proxy RPC to control RPC Services
            with ClusterRpcProxy(config) as rpc:
                response = rpc.serv_controller.controller(query,n_search=5)
                log.debug("-- CRAWLING COMPLETE --")

        except Exception as e:
            log.warning(f"Couldn't connect to Crawler Service, error: {e}")
            return None

        response = json.dumps(response)
        response = response.replace('\\"','"')
        resṕonse = response.replace('\\\\"','\\')


        return response





