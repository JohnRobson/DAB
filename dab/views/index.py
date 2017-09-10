import pandas as pd

from flask import Blueprint, render_template

index = Blueprint('index', __name__)


@index.route('/', methods=['GET', 'POST'])
def main():
    filename = 'advertising'

    df = pd.read_csv('/tmp/{}.csv'.format(filename))


    return render_template('index.html', df=df)
