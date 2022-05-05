#!/usr/bin/env python3
import json
import flask
import redis
from flask import Flask

app = Flask(__name__)


global rd
rd = redis.Redis(host='172.17.0.3', port=6379)


@app.route("/data", methods=["GET", "POST"])
def data() -> str or dict:
    """
    This function responds to a POST curl request and outputs a string
    declaration of success that the data was successfully uploaded to the 
    redis database container. The function also responds to a GET method 
    and returns the redis database item with 'key' key"
    :return: A string declaring success!
    :return: A dictionary of meteorite landing data
    """
    if flask.request.method == "POST":
        with open("Meteorite_Landings.json", 'r') as f:
            d = json.load(f)
            rd.set("key", json.dumps(d))
            return "\n success! \n"
    if flask.request.method == "GET":
        return json.loads(rd.get('key'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
