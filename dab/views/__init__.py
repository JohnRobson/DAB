from flask import render_template, make_response # session, g  # request, redirect, url_for
from dab import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/p01/')
def p01():
    return render_template('p01.html')

