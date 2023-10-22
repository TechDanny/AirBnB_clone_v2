#!/usr/bin/python3
"""starts flask web application"""


from flask import Flask
import re
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
