# -*- coding: utf-8 -*-

__project__ = 'dab'
__version__ = '0.1.dev1'

from flask import Flask  # Blueprint, render_template, make_response, session, g  # request, redirect, url_for
from flask_wtf import CSRFProtect

# from functools import wraps, update_wrapper

# import dab.views.decorators
# from tests.view_decorator import *

app = Flask(__name__) # static_url_path='/static', static_url_path='/static'
app.config.from_pyfile('config.cfg')
app.debug = True

#csrf = CSRFProtect()
#csrf.init_app(app)
app.secret_key = '5accdb11b2c10a78d7c92c5fa102ea77fcd50c2058b00f6e'

################################## Pages ##################################

from .views import static
from .views.index import index
from .views.bot import pbbot
from .views.datasets import datasets

app.register_blueprint(static)
app.register_blueprint(index)
app.register_blueprint(pbbot)
app.register_blueprint(datasets)
# from .util import requests # import dab.util.requests

################################################################################

# from flask_cache import Cache
# app.config['CACHE_TYPE'] = 'null'
# cache = Cache(app,config={'CACHE_TYPE': 'null'})
# @app.route('/')
# @cache.cached(timeout=60)
# def index():

################################################################################


if __name__ == '__main__':
	app.run(debug=False, host='0.0.0.0', port=5050)

# $ python main.py
