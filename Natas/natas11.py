#!/usr/bin/env python3

import requests
import re
import urllib
import base64
import binascii

username = 'natas11'
password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
cookies = { 'data' : 'ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK' }
response = session.post(url, auth = (username, password), cookies = cookies)

# need to reverse $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true); check out natas11.php
# print(binascii.b2a_hex(base64.b64decode(urllib.parse.unquote(session.cookies['data']))))

content = response.text

print(re.findall('natas12 is (.*)<br>', content)[0])