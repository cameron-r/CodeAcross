from flask import Flask, render_template, request, url_for, redirect
import os
import itertools
import sqlite3
from flask import Flask, render_template, request
# from modules.MbtaAPI import MbtaAPI
app = Flask(__name__)


def get_db_conn():
    conn = sqlite3.connect('diplodocus.db')

@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        # stops = MbtaAPI({'verbose': True}).getRoutes(70)
        stops = ['Hello', 'World']
        return render_template('index.html', stops=stops)

    if request.method == "POST":
        return redirect(url_for('search'))

@app.route("/student", methods=["POST"])
def student():

    if request.method == "POST":

        print 'Before', request.form
        student_name = 'Bobby Tables' # TODO: where's it coming from?  request.form['']
        print 'Name:', student_name
        route = request.form['transport_line']
        print 'Route:', route
        direction = request.form['inbound']
        print 'Direction:', direction
        store_student(student_name, route, direction)
        return 'OK'

def store_student(student_name, route, direction):
    
    # TODO: sanitize input!!!

    conn = get_db_conn()
    conn.execute("INSERT INTO students (name, route, direction, delay) VALUES ('{}', '{}', '{}', None)".format(student_name, route, direction, ))


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
