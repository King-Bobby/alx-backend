#!/usr/bin/env python3
"""
Module 6-app.py that Changes your get_locale function
to use a user’s preferred local if it is supported."""


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
    """return user id"""
    return users.get(user_id)


def get_locale():
    """ffunction get_locale"""
    # Check for locale from URL parameters
    requested_locale = request.args.get('locale')
    if requested_locale and requested_locale in app.config['LANGUAGES']:
        return requested_locale

    # Check for locale from user settings
    if g.user and g.user['locale'] and g.user['locale']
    in app.config['LANGUAGES']:
        return g.user['locale']

    # Check for locale from request header
    request_locale = request.headers.get('Accept-Language')
    if request_locale:
        # Extract the first language from the header (format 'en-US,en;q=0.5')
        request_locale = request_locale.split(',')[0].split(';')[0]
        if request_locale in app.config['LANGUAGES']:
            return request_locale

    # Resort to the default locale
    return app.config['BABEL_DEFAULT_LOCALE']


@app.before_request
def before_request():
    """function before_request"""
    # Check if 'login_as' parameter is present in the request
    login_as = request.args.get('login_as')

    # Set the user in flask.g.user if login_as is provided
    g.user = get_user(int(login_as)) if login_as else None

    # Set the selected locale in flask.g.selected_locale
    g.selected_locale = get_locale()


@app.route('/')
def index():
    """connects to html"""
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
