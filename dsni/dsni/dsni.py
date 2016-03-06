from flask import Flask, render_template, request, url_for, redirect
import os
import itertools
from flask import Flask, render_template, request
from modules.MbtaAPI import MbtaAPI
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        stops = MbtaAPI({'verbose': True}).getRoutes(70)
        return render_template('index.html', stops=stops)

    if request.method == "POST":
        return redirect(url_for('search'))

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "GET":
        return render_template('result.html')

    if request.method == "POST":
        #route = request.form['route']

        try:
            mbtaAPIRes = MbtaAPI({'verbose': True}).get()
        except Exception:
            mbtaAPIRes = None

        return render_template('result.html', mbtaAPIRes=mbtaAPIRes)

app.debug = True
if __name__ == "__main__":
    app.run()
