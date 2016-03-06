

"""
Can be nested as an object member of a Vehicle as "vehicle"

      {
        "vehicle_id": "y2292",
        "vehicle_lat": "42.3416976928711",
        "vehicle_lon": "-71.0553283691406",
        "vehicle_bearing": "130",
        "vehicle_speed": "0",
        "vehicle_timestamp": "1457211431"
      },
"""

class Vehicle(object):

    def __init__(self, json):
        self.vehicle_id = json['vehicle_id']
        self.vehicle_lat = json['vehicle_lat']
        self.vehicle_lon = json['vehicle_lon']
        self.vehicle_bearing = json['vehicle_bearing']
        self.vehicle_speed = json['vehicle_speed']
        self.vehicle_timestamp = json['vehicle_timestamp']


