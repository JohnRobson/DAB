# import time
from collections import namedtuple
from io import BytesIO
# import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
from flask import Blueprint, request, render_template, send_file, jsonify  # , make_response
from flask_wtf import csrf, FlaskForm as BaseForm
# from wtforms import SubmitField, StringField, BooleanField
# from wtforms.validators import DataRequired


class Bot(object):
	r""" Bot Class """

	def __init__(self):
		self.df = None

	def read(self, filename):
		self.df = pd.read_csv('db/{}.csv'.format(filename))  # read dataset file

	def commands(self):
		cmd = request.form['command']
		print('Class:', cmd)

		# <p><img src="/plot/Newspaper" alt="Image Placeholder"></p>


bot = Bot()
pbbot = Blueprint('pbbot', __name__)


@pbbot.route('/plot/<col>')
def plot(col):
	print('CALL PLOT')
	ploter = bot.df[[col]].plot()
	# fig, ax = plt.subplots(1)
	fig = ploter.get_figure()
	img = BytesIO()
	fig.savefig(img, format='png', dpi=72, transparent=True)
	img.seek(0)
	return send_file(img, mimetype='image/png')


@pbbot.route('/echo/', methods=['GET'])
def echo():
	ret_data = {"value": request.args.get('echoValue')}
	return jsonify(ret_data)


@pbbot.route('/bot/', methods=['GET', 'POST'])
@pbbot.route('/bot/<int:page>', methods=['GET', 'POST'])
def main(page=1):
	r"""   """
	rt = 'bot.html'
	error = None
	forml = 'bot.main'
	formf = None  # form_bot()
	run = None
	ntm = namedtuple('ntm', 'rt, error, forml, formf, run, df')

	if request.method == 'POST':
		bot.commands()

	#form = PostForm()
	#if form.validate_on_submit():

	bot.read('Advertising')

	nt = ntm(rt, error, forml, formf, run, bot.df)
	return render_template(nt.rt, nt=nt)
