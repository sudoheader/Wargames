#!/usr/bin/env python3

import requests
import re
import base64
import binascii

username = 'natas8'
password = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'

# we need to emulate this php but in reverse: bin2hex(strrev(base64_encode($secret)));
encodedSecret = '3d3d516343746d4d6d6c315669563362'
secret = base64.b64decode(binascii.unhexlify(encodedSecret)[::-1]).decode('utf-8')

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
response = session.post(url, data = { "secret": secret, "submit": "submit" }, auth = (username, password))
content = response.text

# print(content)

print(re.findall('natas9 is (.*)', content)[0])