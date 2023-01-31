#!/usr/bin/python3
"""Starts a flask application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Returns Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Returns C followed by the value of text"""
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_is_fun(text):
    """Returns python followed by the value of text"""
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Returns a n if its an int"""
    return '%d is a number' % n


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
