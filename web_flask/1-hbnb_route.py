#!/usr/bin/python3
"""Starts flask web application"""


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Displays "Hello HBNB!" on the web
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def get_hbnb():
    """
    Displays "HBNB" on the web
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
