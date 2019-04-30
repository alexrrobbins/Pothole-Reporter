import os
import sys
import json
from flask import Flask, render_template, request, redirect, Response

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_coords',methods=['GET','POST'])
def get_coords():
    print(str(request.form.get(key='data')))
    jsdata = request.form['coordjson']

    print(json.loads(jsdata)[0])
    if request.method == "POST":
        print(str(request.form.get(key='data')))
        #latitude = request.get_json()['latitude']
        #longitude = request.get_json()['longitude']
        jsdata = request.form['lat']
        printdata = json.loads(jsdata)
        testvariable = str(printdata)
        return render_template(
            'result.html',
            latitude=testvariable,
            longitude="test")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

app.run(debug=True)
