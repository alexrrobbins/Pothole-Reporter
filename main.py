import os
import sys
import json
from flask import Flask, render_template, request, redirect, Response, jsonify
from coords import Coords
from coordinate_db import add_to_db

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')

app = Flask(__name__)
coordinates = ''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_coords',methods=['GET','POST'])
def get_coords():
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        latitude = request.get_json()['lat']
        longitude = request.get_json()['lng']
        global coordinates
        coordinates = Coords(latitude, longitude)
        return 'OK', 200
    return render_template(
        'result.html',
        latitude="testing",
        longitude="test")

@app.route('/save_coords')
def save_coords():
    global coordinates
    latitude = coordinates.get_lat()
    longitude = coordinates.get_long()
    coordsfile = open('coordsdata.txt','a')
    coordsfile.write('Latitude: ')
    coordsfile.write(str(latitude))
    coordsfile.write('\n')
    coordsfile.write('Longitude: ')
    coordsfile.write(str(longitude))
    coordsfile.write('\n')
    coordsfile.close()
    print('File write complete')
    add_to_db(latitude,longitude)
    return render_template(
            'result.html',
            latitude=str(latitude),
            longitude=str(longitude))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

app.run(debug=True)
