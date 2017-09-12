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

	def commands(self, cmd):
		# cmd = request.form['command']
		cmd = cmd.strip()
		#cmd = cmd.lower()
		cmds = cmd.split(" ")
		print('cmds', cmds)

		if len(cmds) == 0:
			return None

		cmd = cmds[0]
		res = None

		try:
			if cmd == 'help':
				res = """HELP: Available commands:<br />
				<pre>load dataset_name</pre> - load the dataset.<br />
				<pre>ds info</pre> - show the dataset information.<br />
				<pre>plot column_name</pre> - plot the dataset column.<br />
				"""

			if cmd == 'load':
				self.read(cmds[1])
				res = """Data Set (Rows, Columns): <code>""" + str(self.df.shape) + """</code>"""

			if cmd == 'ds':
				if cmds[1] == 'info':
					res = """Data Set Summary:<pre><code>""" + str(self.df.describe()) + """</code></pre></p>"""

			if cmd == 'plot':
				res = """<p><img src="/plot/""" + cmds[1] + """" alt="Image Placeholder"></p>"""

		except Exception as e:
			print('Exception - command:', str(e))

		if res is None:
			res = 'Sorry, I don\'t understand, type: help'

		return '<strong>&lt;DAV&gt;</strong> ' + res


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
	ret = {"value": bot.commands(request.args.get('echoValue'))}
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
