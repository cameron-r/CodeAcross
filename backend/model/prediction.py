
"""
  "route_id": "9",
  "route_name": "9",
  "route_type": "3",
  "mode_name": "Bus",
  "direction": [
    {
      "direction_id": "0",
      "direction_name": "Outbound",
      "trip": [
      ]


    }
  ],
  "alert_headers": []
}

"""
from trip import Trip

class Direction(object):
    """ Nested object within a prediction """
    def __init__(self, json):
        self.direction_id = json['direction_id']
        self.direction_name = json['direction_name']

        self.trips = []

        for trip_elem in json['trip']:
            trip =  Trip(trip_elem)
            self.trips.append(trip)
            
class Prediction(object):

    def __init__(self, json):
        self.route_id = json['route_id']
        self.route_name = json['route_name']
        self.route_type = json['route_type']
        self.mode_name = json['mode_name']

        self.directions = []

        for direction_elem in json['direction']:
            direction = Direction(direction_elem)
            self.directions.append(direction)


