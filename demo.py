import requests

response = requests.get("https://reqres.in/api/users/",
                        params={'page': '2'}, )

print(response.text)
# print(type(response.text))
# print(response.headers)
# print(response.content)

response.status_code = 400
assert requests.ConnectionError
