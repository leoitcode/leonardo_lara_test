import json

from flask import Flask, request
from nameko.rpc import RpcProxy


app = Flask(__name__)

controller = RpcProxy('serv_controller')


@app.route('/crawler/<string:query>')
def get_query(query):

    if query:

        try:
            dicts = self.controller.control(query)

        except Exception as e:
            return "Couldn't connect to Crawler Service"


        return dicts


if __name__ == '__main__':
    app.run(debug=True)






