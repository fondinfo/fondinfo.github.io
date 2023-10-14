import requests

url = 'http://localhost:8000/test.html?name=Turing&born=1912'

resp = requests.get(url)
print(resp.text)

