import requests

getName_response = requests.get("https://restful-booker.herokuapp.com/booking/:id")
print(getName_response.text)

patchName_response = requests.patch("https://postman-echo.com/patch")
print(patchName_response.text)