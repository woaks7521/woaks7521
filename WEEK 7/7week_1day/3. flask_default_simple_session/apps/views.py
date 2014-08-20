from flask import Flask, request, render_template,\
	redirect, url_for, session, g
from apps import app

@app.route('/')
def index():
	if 'user_id' in session :
		return render_template("login.html", username = session['user_id'])
	return render_template("index.html")


@app.route('/Login', methods = ['POST'])
def login():
	id = request.form["id"]
	pw = request.form["pw"]
	
	session.permanent = True
	session['user_id'] = id

	return redirect(url_for('index'))


@app.route('/Logout')
def logout():
	session.clear()
	return redirect(url_for('index'))