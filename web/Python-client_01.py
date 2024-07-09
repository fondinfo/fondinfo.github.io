#!/usr/bin/env python3
"""
@author  Alberto Ferrari - https://albertoferrari.github.io/
@license This software is free - https://opensource.org/license/mit
"""
import requests

response = requests.get("http://localhost:8000/test.html")

if response.ok:
	print("Correct request. response.status_code:",response.status_code)
	print('response.content:\n',response.content)
	print('response.text:\n',response.text)
	print("Content-Type:\n", response.headers["Content-Type"])
	print("Headers:\n", response.headers)
	print('Date:\n', response.headers['Date'])
else:
	print("Error - response.status_code:",response.status_code)

