import requests

response = requests.get("https://reqres.in/api/users/",
                        params={'page': '2'}, )

print(response.text)
print(type(response.text))
# json.loads(response.text)