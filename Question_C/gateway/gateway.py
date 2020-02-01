import json

from flask import Flask, request
from flasgger import Swagger
from nameko.standalone.rpc import ClusterRpcProxy

app = Flask(__name__)
Swagger(app)

CONFIG = {'AMQP_URI': "amqp://guest:guest@localhost:5672"}


@app.route('/crawler/<string:query>')
def get_query(query):

    if query:

        print(query)

        try:

            with ClusterRpcProxy(CONFIG) as rpc:
                query = rpc.serv_controller.controller(query)

        except Exception as e:
            return "Couldn't connect to Crawler Service"


        return query


if __name__ == '__main__':
    app.run(debug=True)






