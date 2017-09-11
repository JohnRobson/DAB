from flask import Blueprint, render_template

static = Blueprint('static', __name__)


@static.route('/contact/', methods=['GET', 'POST'])
def contact():
    r"""   """
    return render_template('contact.html')


@static.route('/features/', methods=['GET', 'POST'])
def features():
    r"""   """
    return render_template('features.html')


@static.route('/help/', methods=['GET', 'POST'])
def help():
    r"""   """
    return render_template('help.html')