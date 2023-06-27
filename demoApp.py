
import requests

responce = requests.get('https://httpbin.org/#/HTTP_Methods/get_get')
print(responce.text)


responce1 = requests.post("https://httpbin.org/#/HTTP_Methods/post_post")
print(responce1)

responce2 = requests.put("https://httpbin.org/#/HTTP_Methods/put_put")
print(responce2)

responce3 = requests.delete("https://httpbin.org/#/HTTP_Methods/delete_delete")
print(responce3)

responce4 = requests.patch('https://httpbin.org/#/HTTP_Methods/patch_patch')
print(responce4)

responce5 = requests.get('https://httpbin.org/#/Status_codes/get_status__codes')
print(responce5)