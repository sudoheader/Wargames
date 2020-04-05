#!/usr/bin/env python3

import requests
import re

username = 'natas2'
password = 'ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'

url = 'http://%s.natas.labs.overthewire.org' % username

response = requests.get(url, auth = (username, password))
content = response.text

print(content)

# print(re.findall('<!--The password for natas3 is (.*) -->', content))