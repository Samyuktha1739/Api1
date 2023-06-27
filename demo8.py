import requests

addName_response = requests.post('https://reqres.in/api/register',
                                 json=
                                 {
                                     "email": "eve.holt@reqres.in",
                                     "password": "pistol"
                                     
                                 }, headers={"Content-Type": "application/json"})

print(addName_response.json())