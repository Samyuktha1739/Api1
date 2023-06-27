import json

import requests


response = requests.get("https://dummy.restapiexample.com/api/v1/employees")

print(response.text)
# print(type(response.text))
# print(response.headers)
# print(response.content)

# dict_response = json.loads(requests.text)
# print(dict_response[0]['Michael'])
