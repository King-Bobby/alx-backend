#!/usr/bin/env python3
"""
Module for a Flask app with Babel extension,
language selection, and forced locale via URL parameters
"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Configuration class for the Flask app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best-matching language based on the user's preferences.

    Returns:
        str: Best-matching language code
    """
    # Check if 'locale' parameter is present in the request
    requested_locale = request.args.get('locale')
    if requested_locale and requested_locale in app.config['LANGUAGES']:
        return requested_locale
    # Resort to the previous default behavior
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Index route that renders the index.html template

    Returns:
        str: Rendered HTML content
    """
    # Get the selected locale using the get_locale function
    selected_locale = get_locale()

    # Pass the selected_locale to the template
    return render_template('4-index.html', selected_locale=selected_locale)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
