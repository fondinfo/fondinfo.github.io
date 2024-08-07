#!/usr/bin/env python3
"""
@author  Alberto Ferrari - https://albertoferrari.github.io/
@license This software is free - https://opensource.org/license/mit
"""
import requests

data = {'q': 'Python'}
r1 = requests.get("https://www.google.com/search", params=data)
r2 = requests.get("https://www.google.com/search?q=Python")

print('time elapsed between sending the request and receiving the response')
print('first  request:',r1.elapsed)
print('second request:',r2.elapsed)

