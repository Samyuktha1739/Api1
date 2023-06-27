import requests

addName_response = requests.put('https://reqres.in/api/users/2',
                                   json=
                                   {
                                      "name": "morpheus",
                                      "job": "zion resident"

                                   }, headers={"Content-Type" : "application/json"})

print(addName_response.json())

# responce_json = addName_response.json()
# print(type(responce_json))
