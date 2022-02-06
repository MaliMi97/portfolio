import time
import requests

class API:
    def __init__(self, time_out, sleep, good_result):
        self.time_out = time_out
        self.sleep = sleep
        self.good_result = good_result
        
    def change_param(self, time_out, sleep):
        self.time_out = time_out
        self.sleep = sleep 
    
    def unit_timestamp(self, date_time):
        return time.mktime(date_time.timetuple())

    def make_request(self, url, *args):
        response = requests.get(url, *args)
        if response.status_code not in self.good_result:
            return {}
        return response.json()
    
    def get_response(self, url, *args):
        response = self.make_request(url, *args)
        if response != {}:
            return response
        seconds = time.time()
        while(response == {}):
            if time.time() - seconds > self.time_out:
                raise Exception("time_out time reached")
            time.sleep(self.sleep)
            response = self.make_request(url, *args)
        return response