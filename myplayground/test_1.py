#!/usr/bin/python3

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello, World!"


@app.route("/<name>", strict_slashes=False)
def hello(name):
    return f"Hello, {escape(name)}!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
