# -*- coding: utf-8 -*-

__project__ = 'dab'
__version__ = '0.1.dev1'


from flask import Flask # render_template, make_response, session, g  # request, redirect, url_for
from flask_wtf import CSRFProtect
# from functools import wraps, update_wrapper


app = Flask(__name__)
app.config.from_pyfile('config.cfg')
app.debug = True

csrf = CSRFProtect()
csrf.init_app(app)

import dab.util.requests
import dab.views
# import dab.views.decorators
# from tests.view_decorator import *

################################################################################

# from flask_cache import Cache
# app.config['CACHE_TYPE'] = 'null'
# cache = Cache(app,config={'CACHE_TYPE': 'null'})
# @app.route('/')
# @cache.cached(timeout=60)
# def index():

################################################################################


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)

# $ python main.py
