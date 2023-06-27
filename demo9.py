import requests

addName_response = requests.post('https://reqres.in/api/register',
                                 json=
                                 {
                                     "email": "peter@klaven"
                                 }, headers={"Content-Type": "application/json"})

print(addName_response.json())