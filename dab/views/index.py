import pandas as pd

from flask import Blueprint, render_template

index = Blueprint('index', __name__)


@index.route('/', methods=['GET', 'POST'])
def main():
    filename = 'Advertising'

    df = pd.read_csv('db/{}.csv'.format(filename))


    return render_template('index.html', df=df)
