from flask import Blueprint, render_template

datasets = Blueprint('datasets', __name__)


@datasets.route('/datasets/', methods=['GET', 'POST'])
def main():
    return render_template('datasets.html')
