import requests as re


base_url = "https://api.nasa.gov/planetary"

endpoint = "/earth/assets"

api_key = "i5XcuLzubzsmuJeSw8yvrveb5PUcJyCRnLD2yzWg"

parameters = {"lat": "29.78", "lon": "-95.33", "date": "2018-01-01", "dim": "0.10", "api_key": api_key}

# endpoint = "https://api.nasa.gov/planetary/apod?api_key=i5XcuLzubzsmuJeSw8yvrveb5PUcJyCRnLD2yzWg"

endpoint_url = base_url + endpoint

# response = re.get(endpoint_url, params=parameters)

# print(response.json())
# print(response.status_code)



dumb_api_call = re.get("https://api.nasa.gov/planetary/earth/imagery?lon=-95.33&lat=29.78&date=2018-01-01&dim=0.15&api_key=DEMO_KEY", stream=True)

import os
import shutil

print(os.getcwd())
# print(dumb_api_call.json())
with open("abcd.png", 'wb') as f:
    shutil.copyfileobj(dumb_api_call.raw, f)
# print('Image sucessfully Downloaded: ', "abcd.png")
































