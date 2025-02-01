class Coords():
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def get_lat(self):
        return self.latitude

    def get_long(self):
        return self.longitude
    
    def get_coords_json(self):
        return {'lat': self.latitude, 'lng': self.longitude}
