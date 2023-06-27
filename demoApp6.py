import requests


myurl = 'https://httpbin.org/post'
files = {'file': ('test.1.txt', 'Welcome to TutorialsPoint')}
getdata = requests.post(myurl, files=files)
print(getdata.text)