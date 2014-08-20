from flask import Flask, request, render_template, make_response,redirect, url_for
from apps import app

@app.route('/')
def index():
	username = request.cookies.get('username')
	if username :
		return render_template("login.html", username = username)
	return render_template("index.html")


@app.route('/Login', methods = ['POST'])
def login():
	id = request.form["id"]
	pw = request.form["pw"]

	resp = make_response(redirect(url_for('index')))
	resp.set_cookie('username',id)
	return resp