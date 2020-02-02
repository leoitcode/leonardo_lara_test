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

        num = request.args.get('num',default = 5,type = int)

        try:

            with ClusterRpcProxy(CONFIG) as rpc:
                response = rpc.serv_controller.controller(query,num)
                print("Query Complete")

        except Exception as e:
            return f"Couldn't connect to Crawler Service, error: {e}"

        response = json.dumps(response)
        response = response.replace('\\"','"')
        resṕonse = response.replace('\\\\"','\\')


        return response


if __name__ == '__main__':
    app.run(debug=True)






