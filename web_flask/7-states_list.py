#!/usr/bin/python3
""" starts a flask web application"""


from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


app.route('/state_list', strict_slashes=False)


def states():
    """
    displays the list of state
    """
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(self):
    """
    deletes the sqlalchemy
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
