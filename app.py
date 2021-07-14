from flask import Flask, redirect, url_for, request
from flask import render_template
app = Flask(__name__)


@app.route('/success')
def success():
    return render_template("thankyou.html")

@app.route('/overview')
def overview():
    return render_template("trackoverview.html")

@app.route('/')
def subscribe():
    return render_template("register.html")

@app.route('/privacy')
def privacy():
    return render_template("privacy.html")    

