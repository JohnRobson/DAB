from os import listdir
from os.path import isfile, join

from flask import Blueprint, render_template

db_dir = 'db'

datasets = Blueprint('datasets', __name__)


@datasets.route('/datasets/', methods=['GET', 'POST'])
def main():

    datasets_files = [f.replace('.csv','') for f in listdir(db_dir) if isfile(join(db_dir, f)) and '.csv' in f] # get all directory elements, keep only CSV files and remove '.csv'

    datasets_files.sort() # sort files names

    return render_template('datasets.html', ds=datasets_files)
