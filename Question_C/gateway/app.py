from flask import Flask, request
import gateway


app = Flask(__name__)


@app.route('/crawler/<string:query>')
def get_query(query):

    #Check args "num" is set
    #num = request.args.get('num',default = 5,type = int)

    response = gateway.start_crawl(query)

    return response


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
