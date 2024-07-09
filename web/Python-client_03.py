#!/usr/bin/env python3
"""
@author  Alberto Ferrari - https://albertoferrari.github.io/
@license This software is free - https://opensource.org/license/mit
"""
import requests
url = 'http://localhost:8000/example.js'
x = requests.get(url)
print(x.text,type(x.text))
print(x.json(),type(x.json()))

