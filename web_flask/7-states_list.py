#!/usr/bin/python3
"""
Starts a Flask web application.
"""
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """
    This function is called after each request to the application.
    It closes the current SQLAlchemy session to ensure that connections are properly closed.
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    This route responds to requests for '/states_list'.
    It retrieves all State objects from the storage, then renders an HTML template
    called '7-states_list.html', passing the list of states to the template.
    """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
