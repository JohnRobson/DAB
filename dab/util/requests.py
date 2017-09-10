from flask import session, g
from werkzeug.http import http_date
from datetime import datetime
from dab import app


@app.before_request
def load_user():
    if 'user_id' in session and session['user_id']:
        # user = User.query.filter_by(username=session['user_id']).first()
        pass
    else:
        user = {'name': 'Guest'}  # Make it better, use an anonymous User instead

    g.user = user


@app.after_request
def add_header(r):
    r.headers['Cache-Control'] = 'public, no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    r.headers['Last-Modified'] = http_date(datetime.now())
    r.headers['Pragma'] = 'no-cache'
    r.headers['Expires'] = '0'
    r.cache_control.max_age = 0
    r.cache_control.public = True
    return r
