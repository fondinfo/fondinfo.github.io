import requests
url = 'http://localhost:8000/example.js'
x = requests.get(url)
print(x.text,type(x.text))
print(x.json(),type(x.json()))

