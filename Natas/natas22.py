#!/usr/bin/env python3

import requests
import re

username = 'natas22'
password = 'chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ'

url = 'http://%s.natas.labs.overthewire.org/?revelio=1' % username

session = requests.Session()

response = session.get(url, auth = (username, password), allow_redirects = False)
# print(response.text)
print(re.findall('Password: (.*)</pre>', response.text)[0])