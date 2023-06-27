import requests

# myurl = "https://jsonplaceholder.typicode.com/users"
# myparams = {'name': 'ABC', 'email': 'xyz@gmail.com'}
# res = requests.get(myurl, data=myparams)
# print(res.text)
# print(res)
#
#
# payload = {'id': 9, 'username': 'Delphine'}
# getdata = requests.get('https://jsonplaceholder.typicode.com/users',
#                        params=payload)
# print(getdata.content)
# print(getdata.text)
#
# post = 'https://postman-echo.com/post'
# postName_data = {'name': 'ABC', 'email': 'xyz@gmail.com'}
# postName_response = requests.post(post, data=postName_data)
# print(postName_response.text)

put = 'https://postman-echo.com/put'
putName_data = {'name': 'ABC', 'email':'xyz@gmail.com'}
putName_response = requests.put(put, data=putName_data)
print(putName_response.text)
