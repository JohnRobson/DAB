#!/usr/bin/env python3

import os, gc  # sys
from flask import request
from dab import app  # dt


def run_server():
	port = int(os.environ.get('PORT', 5050))
	# app, sess, dt, mail = create_app().app_context().push()
	# app, sess, dt, mail = create_app()
	app.run(host='0.0.0.0', port=port, use_reloader=True, threaded=True)  # debug=True, processes=4


def shutdown_server():
	func = request.environ.get('werkzeug.server.shutdown')
	if func is None:
		raise RuntimeError('Not running with the Werkzeug Server')
	func()


if __name__ == '__main__':
	# print('Datetime:', dt())
	gc.collect()
	run_server()


'''
server = Process(target=app.run)
server.start()
# ...
server.terminate()
server.join()
'''
