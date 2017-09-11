from os import listdir
from os.path import isfile, join
from collections import namedtuple
import time
from flask import Blueprint, render_template

datasets = Blueprint('datasets', __name__)
db_dir = 'db'


def read_dataset_files():
	r""" read dataset files and return the cvs files  """
	datasets_files = [f[:-4] for f in listdir(db_dir) if
	 isfile(join(db_dir, f)) and '.csv' in f]  # get all directory elements, keep only CSV files and remove '.csv' # .replace('.csv', '')
	datasets_files.sort()  # sort files names
	return datasets_files


@datasets.route('/datasets/', methods=['GET', 'POST'])
def main():
	r"""   """
	rt = 'datasets.html'
	error = None
	forml = 'datasets.main'
	formf = None  # form_bot()
	run = None
	ntm = namedtuple('ntm', 'rt, error, forml, formf, run, datasets_files')

	datasets_files = read_dataset_files()

	nt = ntm(rt, error, forml, formf, run, datasets_files)
	return render_template(nt.rt, nt=nt)
