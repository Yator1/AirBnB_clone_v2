#!/usr/bin/python3

"""
A script that starts a flask web app
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_flask():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    text = text.replace('_', ' ')
    return f"C {text}"

if __name__ == '__main__':
    app.run(debug=True)
