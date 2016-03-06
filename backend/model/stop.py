

"""

Can be nested as a member of a list of stops 
under a prediction's ["direction"]["trip"]["stop"]

            {
              "stop_sequence": "12",
              "stop_id": "11532",
              "stop_name": "W Broadway @ Linsky Barry Ct",
              "sch_arr_dt": "1457211540",
              "sch_dep_dt": "1457211540",
              "pre_dt": "1457211500",
              "pre_away": "13"
            },

"""

class Stop(object):

    def __init__(self, json):
        self.stop_sequence = int(json['stop_sequence'])
        self.stop_id = json['stop_id']
        self.stop_name = json['stop_name']
        self.sch_arr_dt = int(json['sch_arr_dt'])
        self.sch_dep_dt = int(json['sch_dep_dt'])
        self.pre_dt = int(json['pre_dt'])
        self.pre_away = int(json['pre_away'])


