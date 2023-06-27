import requests

addName_response = requests.delete('https://reqres.in/api/users/2',
                                   json=
                                   {
                                      "name": "morpheus",
                                      "job": "zion resident"

                                   }, headers={"Content-Type" : "application/json"})

# print(addName_response.json())