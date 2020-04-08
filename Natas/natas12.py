#!/usr/bin/env python3

import requests
import re
import urllib
import base64
import binascii

username = 'natas12'
password = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
# response = session.post(url, auth = (username, password), cookies = cookies)
response = requests.get(url, auth = (username, password))

content = response.text

print(content)

# print(re.findall('natas12 is (.*)', content)[0])