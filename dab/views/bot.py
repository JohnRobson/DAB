# import time
from collections import namedtuple
from io import BytesIO
import base64
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

	def plot(self, format, col):
		r""" :type 1 = image, 2 = data"""
		if col in self.df.columns:
			ploter = bot.df[[col]].plot(figsize=(6, 4), fontsize=10)
			# fig, ax = plt.subplots(1)
			fig = ploter.get_figure()
			img = BytesIO()
			fig.savefig(img, format='png', dpi=100, transparent=True, edgecolor='k', bbox_inches='tight')  # facecolor='w'
			img.seek(0)
			if format == 1: return img
			if format == 2: return base64.b64encode(img.getvalue()).decode('UTF-8')

		return None

	def commands(self, cmd):
		# cmd = request.form['command']
		cmds = cmd.strip().split(' ') # .lower()
		print('cmds', cmds)

		if len(cmds) == 0:
			return None

		cmd = cmds[0].lower()
		res = None

		try:
			if cmd == 'help':
				res = """Available commands:<br />
				<code>load dataset_name</code> - load the dataset.<br />
				<code>ds info</code> - show the dataset information.<br />
				<code>plot column_name</code> - plot the dataset column.<br />
				"""

			if cmd == 'load':
				self.read(cmds[1])
				res = 'Data Set (Rows, Columns): <code>' + str(self.df.shape) + '</code>'

			if cmd == 'ds':
				if cmds[1] == 'info':
					res = 'Data Set Summary:<pre><code>' + str(self.df.describe()) + '</code></pre></p>'

			if cmd == 'plot':
				data = bot.plot(2, cmds[1])
				if data is not None:
					res = '<div class="virtualPlaceholder"><img src="data:image/png;base64,{}" alt="Image Placeholder"></div>'.format(data)
				else:
					res = 'Sorry, this column <code>' + cmds[1] + '</code> doesn\'t exist.'

		except Exception as e:
			print('Exception - command:', str(e))
			res = 'Sorry, this command syntax is wrong, check: <code>help</code>'

		finally:
			pass

		if res is None:
			res = 'Sorry, I don\'t understand, type: help'

		return '<img src="/static/img/dab.png" height="25"/> ' + res


bot = Bot()
pbbot = Blueprint('pbbot', __name__)


@pbbot.route('/plot/<col>')
def plot(col): # http://0.0.0.0:5050/plot/Balance
	img = bot.plot(1, col)
	if img is not None:
		return send_file(img, mimetype='image/png')

@pbbot.route('/echo/', methods=['GET'])
def echo():
	ret = {'value': bot.commands(request.args.get('echoValue'))}
	return jsonify(ret)


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

	nt = ntm(rt, error, forml, formf, run, bot.df)
	return render_template(nt.rt, nt=nt)
