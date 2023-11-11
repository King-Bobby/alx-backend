#!/usr/bin/env python3
"""
Module for a basic Flask app
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index() -> str:
    """
    Index route that renders the index.html template

    Returns:
        str: Rendered HTML content
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
