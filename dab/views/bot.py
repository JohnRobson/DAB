import pandas as pd
from flask import Blueprint, render_template

bot = Blueprint('bot', __name__)


@bot.route('/bot/', methods=['GET', 'POST'])
def main():
    filename = 'Advertising'

    df = pd.read_csv('db/{}.csv'.format(filename))

    return render_template('bot.html', df=df)
