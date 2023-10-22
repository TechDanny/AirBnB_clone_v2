#!/usr/bin/python3
"""Starts a flask web application"""


import re
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    displays "Hello HBNB!" on the web
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def get_hbnb():
    """
    displays "HBNB" on the web
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_text(text):
    """
    displays a text
    """
    text_with_space = re.sub('_', ' ', text)
    return f"C {text_with_space}"


@app.route("/python/", defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """
    displays python text
    """
    text_with_space = re.sub('_', ' ', text)
    return f"Python {text_with_space}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
