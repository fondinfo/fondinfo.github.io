#!/usr/bin/env python3
"""
@author  Alberto Ferrari - https://albertoferrari.github.io/
@license This software is free - https://opensource.org/license/mit
"""
import requests
url = 'http://localhost:8000'
myData = {'author': 'Van Rossum'}

x = requests.post(url, json = myData)
print(x.text)
