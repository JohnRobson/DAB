from flask import render_template, make_response # session, g  # request, redirect, url_for
from dab import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/datasets/')
def datasets():
    return render_template('datasets.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/features/')
def features():
    return render_template('features.html')

@app.route('/help/')
def help():
    return render_template('help.html')
