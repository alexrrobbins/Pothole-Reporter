import os
import sys
from flask import Flask, render_template, request, redirect, Response

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result',methods=['POST'])
def worker():
    latitude = request.index['latitude']
    longitude = request.index['longitude']
    return render_template(
        'result.html',
        latitude=latitude,
        longitude=longitude)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

app.run(debug=True)
