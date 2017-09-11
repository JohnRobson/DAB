from os import listdir
from os.path import isfile, join
from collections import namedtuple
import time
from flask import Blueprint, render_template

datasets = Blueprint('datasets', __name__)
db_dir = 'db'


@datasets.route('/datasets/', methods=['GET', 'POST'])
def main():
	rt = 'datasets.html'
	error = None
	forml = 'datasets.main'
	formf = None  # form_bot()
	run = None
	ntm = namedtuple('ntm', 'rt, error, forml, formf, timestamp, run, datasets_files')

	datasets_files = [f.replace('.csv', '') for f in listdir(db_dir) if isfile(join(db_dir, f)) and '.csv' in f]  # get all directory elements, keep only CSV files and remove '.csv'

	datasets_files.sort()  # sort files names

	nt = ntm(rt, error, forml, formf, str(time.time()), run, datasets_files)
	return render_template(nt.rt, nt=nt)
