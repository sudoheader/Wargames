#!/usr/bin/env python3

import requests
import re
import base64
import urllib

username = 'natas28'
password = 'JWwR438wkgTsNKBbcJoowyysdM82YjeF'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
# response = session.get(url, auth = (username, password))

block_size = 16

# for i in range(16): # FIXME: Try 12-13 later
# 	response = session.post(url, data = { "query": "a"*i }, auth = (username, password))

# 	print("query_length:", i, ", response_length:", len(base64.b64decode(requests.utils.unquote(response.url[60:]))))

# 	print('='*50)
# 	for block in range(int(80 / block_size)):
# 		print("block", block + 1, "data", repr(base64.b64decode(requests.utils.unquote(response.url[60:]))[block * block_size:(block + 1) * block_size]))

import string

correct_string = repr(b'\x9eb&\x86\xa5&@YW\x06\t\x9a\xbc\xb0R\xbb')
for c in string.printable:
	print("trying", c)
	response = session.post(url, data = { "query": "a"*9+c }, auth = (username, password))

	block = 2 # 0-based
	answer = repr(base64.b64decode(requests.utils.unquote(response.url[60:]))[block * block_size:(block + 1) * block_size])
	if answer == correct_string:
		print("WE FOUND THE CHARACTER", c)

# print(repr(base64.b64decode(requests.utils.unquote(response.url[60:]))))
# print(base64.b64decode(requests.utils.unquote(response.url[60:])))
# print(response.text)
# print(re.findall('=&gt; (.*)\n', response.text)[1])