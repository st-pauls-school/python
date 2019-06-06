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
		mymodule = importlib.import_module(m)
		headlines.append({'module' : m, 'headline' : mymodule.headline()})


	return render_template('dashboard.html', title='5th Form Summer Dashboard', headlines=headlines)
