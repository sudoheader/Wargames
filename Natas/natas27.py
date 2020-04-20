#!/usr/bin/env python3

import requests
import re
import base64
import urllib

username = 'natas27'
password = '55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
response = session.get(url, auth = (username, password))

print(response.text)
# print(re.findall('(.*)', response.text)[0])