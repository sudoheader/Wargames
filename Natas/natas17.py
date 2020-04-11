#!/usr/bin/env python3

import requests
import re
from string import *

characters = ascii_lowercase + ascii_uppercase + digits

username = 'natas17'
password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'

url = 'http://%s.natas.labs.overthewire.org/index-source.html' % username

session = requests.Session()

response = requests.get(url, auth = (username, password))
content = response.text

print(content)
# print(re.findall('natas15 is (.*)<br>', content)[0])