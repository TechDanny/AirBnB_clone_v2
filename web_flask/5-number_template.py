#!/usr/bin/python3
"""Starts a flask web application"""


import re
from flask import Flask, render_template
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


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """
    displays a number on the web
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_temp(n):
    """
    Gets html file
    """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
