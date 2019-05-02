import json
from flask import Flask, render_template, request, redirect, Response, jsonify
from coords import Coords
from coordinate_db import add_to_db

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

@app.route('/save_coords')
def save_coords():
    global coordinates
    latitude = coordinates.get_lat()
    longitude = coordinates.get_long()
    add_to_db(latitude,longitude)
    return render_template(
            'result.html',
            latitude=str(latitude),
            longitude=str(longitude))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

app.run(debug=True)
