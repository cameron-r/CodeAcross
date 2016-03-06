
import json
import requests
from prediction import Prediction

# import Config


MBTA_REALTIME_URI = 'http://realtime.mbta.com/developer/api/v2/{}?api_key={}'

class MbtaQueryPerformer(object):
    def __init__(self):
        self.api_key = 'wX9NwuHnZU2ToO7GmGR9uw'

    def query_schedule(self, route, direction):
        uri = MBTA_REALTIME_URI.format('schedulebyroute', self.api_key)
        uri += '&route={}&direction={}'.format(route, direction)
        r = requests.get(uri)

        print r.text

    def query_predictions(self, route, direction):
        uri = MBTA_REALTIME_URI.format('predictionsbyroute', self.api_key)
        uri += '&route={}&direction={}'.format(route, direction)
        r = requests.get(uri)

        # print r.text
        # print r.status_code
        prediction = Prediction(json.loads(r.text))

        lateness = 0
        bus_count = 0
        for dir in prediction.directions:
            for trip in dir.trips:
                bus_count += 1
                largest_delta = 0
                for stop in trip.stops:
                    delta = stop.pre_dt - stop.sch_arr_dt
                    if delta > largest_delta:
                        largest_delta = delta

                lateness += largest_delta


        print 'Total', lateness
        print 'Avg', lateness / bus_count
        return prediction


def main():
    doer = MbtaQueryPerformer()
    # doer.query_predictions(9, 0)
    doer.query_schedule(9, 0)

main()



