#!/usr/bin/env python3
"""
@author  Alberto Ferrari - https://albertoferrari.github.io/
@license This software is free - https://opensource.org/license/mit
"""
import requests

url = 'http://localhost:8000/test.html?name=Turing&born=1912'

resp = requests.get(url)
print(resp.text)

