import time
from collections import namedtuple
from io import BytesIO
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from flask import Blueprint, render_template, send_file  # , make_response


class Bot(object):
	r""" Bot Class """

	def __init__(self):
		self.df = None

	def read(self, filename):
		self.df = pd.read_csv('db/{}.csv'.format(filename))  # read dataset file


bot = Bot()
pbbot = Blueprint('pbbot', __name__)


@pbbot.route('/plot/<col>')
def plot(col):
	ploter = bot.df[[col]].plot()
	# fig, ax = plt.subplots(1)
	fig = ploter.get_figure()
	img = BytesIO()
	fig.savefig(img, format='png', dpi=72, transparent=True)
	img.seek(0)
	return send_file(img, mimetype='image/png')


@pbbot.route('/bot/', methods=['GET', 'POST'])
def main():
	r"""   """
	rt = 'bot.html'
	error = None
	forml = 'bot.main'
	formf = None  # form_bot()
	run = None
	ntm = namedtuple('ntm', 'rt, error, forml, formf, run, df')

	bot.read('Advertising')

	nt = ntm(rt, error, forml, formf, run, bot.df)
	return render_template(nt.rt, nt=nt)
