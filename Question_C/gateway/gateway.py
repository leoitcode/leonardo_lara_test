import json

from flask import Flask, request
from flasgger import Swagger
from nameko.standalone.rpc import ClusterRpcProxy
from loguru import logger as log


app = Flask(__name__)
Swagger(app)

CONFIG = {'AMQP_URI': "amqp://guest:guest@localhost:5672"}

log_file_name = './logs/' + 'crawler' + '.log'

log.add(
    log_file_name,
    level="DEBUG",
    backtrace=True,
    diagnose=True,
    rotation="00:00"
    )


@app.route('/crawler/<string:query>')
def get_query(query):

    if query:

        log.info("-- STARTING THE CRAWLER --")

        num = request.args.get('num',default = 5,type = int)

        try:

            with ClusterRpcProxy(CONFIG) as rpc:
                response = rpc.serv_controller.controller(query,num)
                log.debug("-- CRAWLING COMPLETE --")

        except Exception as e:
            log.warning(f"Couldn't connect to Crawler Service, error: {e}")
            return None

        response = json.dumps(response)
        response = response.replace('\\"','"')
        resṕonse = response.replace('\\\\"','\\')


        return response


if __name__ == '__main__':
    app.run(debug=True)






