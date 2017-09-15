# import time
import os.path
from io import BytesIO
import base64
from collections import namedtuple
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
		self.df = pd.DataFrame()

	def read(self, filename):
		if os.path.isfile('db/{}.csv'.format(filename)): # check if file exists
			try:
				self.df = pd.read_csv('db/{}.csv'.format(filename))  # read dataset file
			except Exception as e:
				print('Exception - read dataset:', str(e))
		return None

	def plot(self, format, col):
		r""" :type 1 = image, 2 = data"""
		if not self.df.empty and col in self.df.columns:
			ploter = self.df[[col]].plot(figsize=(6, 4), fontsize=10)
			# fig, ax = plt.subplots(1)
			fig = ploter.get_figure()
			img = BytesIO()
			fig.savefig(img, format='png', dpi=100, transparent=True, edgecolor='k', bbox_inches='tight')  # facecolor='w'
			img.seek(0)
			if format == 1: return img
			if format == 2: return base64.b64encode(img.getvalue()).decode('UTF-8')
		return None

	def commands(self, line):
		print('DEBUG 1', line)
		# cmd = request.form['command']
		cmds = line.strip().split(' ') # .lower()
		print('cmds', cmds)

		if len(cmds) == 0:
			return None

		cmd = cmds[0].lower()
		rt = None
		print('DEBUG 2', cmd)

		try:
			if cmd == 'help':
				rt = """Available commands:<br />
				<code>load dataset_name</code> - load the dataset.<br />
				<code>ds info</code> - show the dataset information.<br />
				<code>plot column_name</code> - plot the dataset column.<br />
				<code>calc</code> - do a basic arithmetic operation.<br />
				"""

			if cmd == 'load':
				self.read(cmds[1])
				if not self.df.empty:
					rt = 'Data Set (Rows, Columns): <code>' + str(self.df.shape) + '</code>'
				else:
					rt = 'Data Set doesn\'t exist.'

			if cmd == 'ds':
				if cmds[1] == 'info':
					if not self.df.empty:
						rt = 'Data Set Summary:<pre><code>' + str(self.df.describe()) + '</code></pre></p>'
					else:
						rt = 'Load some dataset first: <code>load dataset_name</code>'

			if cmd == 'plot':
				data = self.plot(2, cmds[1])
				if data is not None:
					#rt = '<img src="data:image/png;base64,{}" width="533" height="355" alt="Image Placeholder">'.format(data)
					rt = '<img src="/plot/{}" width="533" height="355" alt="Image Placeholder">'.format(cmds[1])
				else:
					rt = 'Sorry, this column <code>' + cmds[1] + '</code> doesn\'t exist.'

		except Exception as e:
			print('Exception - command:', str(e))
			rt = 'Sorry, this command syntax is wrong, check: <code>help</code>'

		finally:
			pass

		if cmd == 'calc':
			rt = str(eval(' '.join(cmds[1:])))

		if rt is None:
			rt = 'Sorry, I don\'t understand what you said, type: <code>help</code>'

		rt = '<img src="/static/img/dab.png" height="25"/>' \
				 '<div class="bubble"><code>&gt; ' + line + '</code><br /><br />' + rt + '</div>'

		return rt


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

	#if request.method == 'POST':
	#	bot.commands()

	#form = PostForm()
	#if form.validate_on_submit():

	nt = ntm(rt, error, forml, formf, run, bot.df)
	return render_template(nt.rt, nt=nt)
