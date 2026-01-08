import json
import os
from json import loads

import requests

is_exist = os.path.isfile("data/user_data.json")
print (is_exist)

url_base = 'https://petstore.swagger.io/v2/'
headers = {'Content-Type':'application/json'}
f = open('data/user_data.json')      # Opening JSON file
data_from_file = json.load(f)  # returns JSON as object

# data = json.dump(open("data/user_data.json"))


response = requests.post(url_base+'user',headers=headers, data=data_from_file)
print (response.status_code)

print (is_exist)