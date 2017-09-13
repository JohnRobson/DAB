import sys, os
from setuptools import setup, find_packages

setup(
	name='dab',
	version='0.1.dev1',
	license='AGPLv3',
	author='John Robson',
	author_email='jleiteja@stevens.edu',
	url='https://dab42.herokuapp.com/',
	description=('DAB - Data Analysis Bot'),
	keywords=('data, bot'),
	long_description='README',
	packages=find_packages(),
	install_requires=[
		'flask',
		'uwsgi',
	],
	classifiers=[
		'Development Status :: 2 - Pre-Alpha',
		'Intended Audience :: Developers',
		'Intended Audience :: Education',
		'Programming Language :: Python',
	],
	include_package_data=True,
	zip_safe=False,
)

# develop='no-deps',
# packages=['dab'],

# entry_points={ 'invenio.config': ['myoverlay = myoverlay.config'] }

# pip install git+git://github.com/inveniosoftware/invenio@pu#egg=Invenio-dev -e .

# package_data =
#        { 'rocky_server' :        # NOTE: package/folder name, not pip name
#          [ 'templates/*.html'
#          , 'static/favicon.ico'
#          , 'static/*.png'
#          ]
#        }

# classifiers=[

# test_suite="lmod_proxy.tests",
# tests_require=tests_require,
# cmdclass={"test": PyTest},
# zip_safe=False,


if __name__ == '__main__':
	try:
		setup()
		sys.exit(0)
	except SystemExit as e:
		os._exit(0)
