import time
from collections import namedtuple
from io import BytesIO
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import prettyplotlib as ppl
from flask import Blueprint, render_template, send_file  # , make_response

bot = Blueprint('bot', __name__)


@bot.route('/img/<img>')
def img(img):
	fig, ax = plt.subplots(1)
	ppl.bar(ax, np.arange(10), np.abs(np.random.randn(10)))
	img = BytesIO()
	fig.savefig(img, format='png', dpi=72)
	img.seek(0)
	return send_file(img, mimetype='image/png')


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


