from flask import Blueprint, render_template

index = Blueprint('index', __name__)


@index.route('/')
def main():
	r"""   """
	return render_template('index.html')
