from flask import Flask
from flask import render_template
from flask_breadcrumbs import Breadcrumbs, register_breadcrumb
from flask import request
from forms import *
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
Breadcrumbs(app=app)


@app.route('/')
@register_breadcrumb(app, '.', 'Home')
def home():
    return render_template('home.html')

@app.route('/requests')
@register_breadcrumb(app, '.requests', 'Requests')
def requests():
	return render_template('requests/index.html')

@app.route('/requests/create')
@register_breadcrumb(app, '.requests.create', 'Create')
def requests_create():
	form = RequestForm(request.form)
	return render_template('requests/create.html',form=form)

@app.route('/requests/store', methods=["POST"])
def requests_store():
	form = AngelForm(request.form)

	if form.validate():
		pass
	else:
		return render_template('requests/create.html',form=form)

	return request.form['name']

@app.route('/angels')
@register_breadcrumb(app, '.angels', 'Angels')
def angels():
	return render_template('angels/index.html')

@app.route('/angels/create')
@register_breadcrumb(app, '.angels.create', 'Create')
def angels_create():
	form = AngelForm(request.form)
	return render_template('angels/create.html',form=form)

@app.route('/angels/store', methods=["POST"])
def angels_store():
	form = AngelForm(request.form)

	if form.validate():
		pass
	else:
		return render_template('angels/create.html',form=form)
