import requests


myurl = 'https://httpbin.org/post'
files = {'file': open('test.2', 'r+b')}
getdata = requests.post(myurl, files=files)
print(getdata.text)