import requests

myurl = 'https://postman-echo.com/put'
myparams = {'name': 'ABC', 'email':'xyz@gmail.com'}
res = requests.put(myurl, data=myparams)
print(res.text)
print(res)

patchNmae = "https://postman-echo.com/patch"
patchNmae_response = requests.patch(patchNmae, data="testing patch")
print(patchNmae_response.text)
print(patchNmae_response)

delete = 'https://postman-echo.com/delete'
delete_response = requests.delete(delete, data="testing delete")
print(delete_response.text)
print(delete_response)