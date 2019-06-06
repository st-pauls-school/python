from app import app
from flask import render_template
from flask import request
import importlib

@app.route('/')
@app.route('/index')
def index():
	modules = ['sample']
	headlines = []
	for m in modules: 
		# run the module code - https://stackoverflow.com/questions/8718885/import-module-from-string-variable 
		mymodule = importlib.import_module(m)

		# The incoming HTML needs to be handled carefully - it will be assumed safe, which might be dangerous 
		#   https://stackoverflow.com/a/28489615/2902 
		headlines.append({'module' : m, 'headline' : mymodule.headline()})


	return render_template('dashboard.html', title='5th Form Summer Dashboard', headlines=headlines)
