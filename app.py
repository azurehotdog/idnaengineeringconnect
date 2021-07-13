from flask import Flask, redirect, url_for, request
from flask import render_template
app = Flask(__name__)


@app.route('/success')
def success():
    return render_template("thankyou.html")

@app.route('/')
def subscribe():
    return render_template("subscribe.html")

@app.route('/unsubscribe')
def unsubscribe():
    return render_template("unsubscribe.html")

@app.route('/unsubscribesuccess')
def unsubscribesuccess():
    return render_template("sorrytoseeyougo.html")


