

"""
Can be nested as a member of a list of trips 
under a prediction's ["direction"]["trip"]

        {
          "trip_id": "29158768",
          "trip_name": "3:45 pm from Boylston St @ Dartmouth St to City Point Bus Terminal",
          "trip_headsign": "City Point",
          "vehicle": {
            "vehicle_id": "y2292",
            "vehicle_lat": "42.3416976928711",
            "vehicle_lon": "-71.0553283691406",
            "vehicle_bearing": "130",
            "vehicle_speed": "0",
            "vehicle_timestamp": "1457211431"
          },
          "stop": []
"""
from stop import Stop
from vehicle import Vehicle

class Trip(object):

    def __init__(self, json):
        self.trip_id = json['trip_id']
        self.trip_name = json['trip_name']
        self.trip_headsign = json['trip_headsign']

        # It seems Vehicles do not get assigned to trips until
        # they are enroute
        try:
            self.vehicle = Vehicle(json['vehicle'])
        except KeyError:
            self.vehicle = None

        self.stops = []
        for stop_elem in json['stop']:
            stop = Stop(stop_elem)
            self.stops.append(stop)
