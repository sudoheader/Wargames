#!/usr/bin/env python3

import requests
import re
import binascii

username = 'natas20'
password = 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

response = requests.get(url, auth = (username, password))

print(response.text)