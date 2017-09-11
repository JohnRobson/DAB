from collections import namedtuple
import time
import pandas as pd
from flask import Blueprint, render_template

bot = Blueprint('bot', __name__)


@bot.route('/bot/', methods=['GET', 'POST'])
def main():
	r"""   """
	rt = 'bot.html'
	error = None
	forml = 'bot.main'
	formf = None  # form_bot()
	run = None
	ntm = namedtuple('ntm', 'rt, error, forml, formf, run, df')

	filename = 'Advertising'  # dataset file

	df = pd.read_csv('db/{}.csv'.format(filename))  # read dataset file

	nt = ntm(rt, error, forml, formf, run, df)
	return render_template(nt.rt, nt=nt)
