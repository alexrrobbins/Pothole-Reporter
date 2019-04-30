import os
import sys
import json
from flask import Flask, render_template, request, redirect, Response, jsonify

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
    if request.method == 'POST':
        print('Incoming..')
        print(request.get_json())  # parse as JSON
        print(request.get_json()['lat'])
        print(request.get_json()['lng'])
        return 'OK', 200
    return render_template(
        'result.html',
        latitude="testing",
        longitude="test")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

app.run(debug=True)
