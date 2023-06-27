import requests

url = "https://example.com"

# Use the following format for the username and password: "username:password"
credentials = "user:pass"

headers = {
    "Authorization": f"Basic {credentials}"
}

response = requests.get(url, headers=headers)

print(response.status_code)