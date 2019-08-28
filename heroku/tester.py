import json
import requests

# url = "http://localhost:5000"  # if you want to test local
url = "http://diabetes-manager-app.herokuapp.com"  # if you want to test deployed

val = [{"timestamp": '2000-10-10 8:10',
        "code": 33,
        "value": 10.0,
        "user_id": 1},
       {"timestamp": '2000-10-10 8:10',
        "code": 59,
        "value": 100.0,
        "user_id": 1},
       {"timestamp": '2000-10-10 12:10',
        "code": 60,
        "value": 180.0,
        "user_id": 1},
       {"timestamp": '2000-10-10 20:10',
        "code": 63,
        "value": 250.0,
        "user_id": 1},
       {"timestamp": '2000-10-10 23:10',
        "code": 57,
        "value": 300.0,
        "user_id": 1},
       {"timestamp": '2000-10-11 8:10',
        "code": 33,
        "value": 10.0,
        "user_id": 1},
       {"timestamp": '2000-10-11 8:10',
        "code": 59,
        "value": 100.0,
        "user_id": 1},
       {"timestamp": '2000-10-11 12:10',
        "code": 60,
        "value": 180.0,
        "user_id": 1},
       {"timestamp": '2000-10-11 20:10',
        "code": 63,
        "value": 250.0,
        "user_id": 1},
       {"timestamp": '2000-10-11 23:10',
        "code": 57,
        "value": 300.0,
        "user_id": 1},
       {"timestamp": '2000-10-12 8:10',
        "code": 33,
        "value": 10.0,
        "user_id": 1},
       {"timestamp": '2000-10-12 8:10',
        "code": 59,
        "value": 100.0,
        "user_id": 1},
       {"timestamp": '2000-10-12 12:10',
        "code": 60,
        "value": 180.0,
        "user_id": 1},
       {"timestamp": '2000-10-12 20:10',
        "code": 63,
        "value": 250.0,
        "user_id": 1},
       {"timestamp": '2000-10-12 23:10',
        "code": 57,
        "value": 300.0,
        "user_id": 1}]


# you'll get a 200 response if the keys align, and something bad if the keys don't align.

if __name__ == '__main__':
    r_success = requests.post(url, data=json.dumps(val))
    print(
        f"Request responded: {r_success}.\nThe content of the resonse was {r_success.json()}")
