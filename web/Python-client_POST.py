import requests
url = 'http://localhost:8000'
myData = {'author': 'Van Rossum'}

x = requests.post(url, json = myData)
print(x.text)
