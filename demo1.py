import json

import jsonpath
import requests

response = requests.get("https://reqres.in/api/users/",
                        params={'page': '2'}, )


json_response = json.loads(response.text)
print(json_response)
pages = jsonpath.jsonpath(json_response, "total_pages")
print(pages[0])
assert pages[0] == 2