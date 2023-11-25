#!/usr/bin/env python3
"""
Module for a Flask app with Babel extension
"""


from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """returns user.id"""
    return users.get(user_id)


@app.before_request
def before_request():
    """function before_request"""
    # Check if 'login_as' parameter is present in the request
    login_as = request.args.get('login_as')

    # Set the user in flask.g.user if login_as is provided
    g.user = get_user(int(login_as)) if login_as else None


@app.route('/')
def index():
    """Connects to html"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
