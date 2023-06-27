import requests

addName_response = requests.post('https://reqres.in/api/users',
                                 json=
                                 {
                                     "name": "morpheus",
                                     "job": "leader"

                                 }, headers={"Content-Type": "application/json"})

print(addName_response.json())