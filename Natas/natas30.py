#!/usr/bin/env python3

import requests
import re
import base64

username = 'natas30'
password = 'wie9iexae0Daihohv8vuu3cei9wahf0e'

# url = 'http://%s.natas.labs.overthewire.org/index.pl?file=/etc/natas_webpass/natas30' % username
url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
response = session.get(url, auth = (username, password))

# response = session.post(url, auth = (username, password))

print(response.text)
# print(re.findall('</html>\n(.*)\n', response.text)[0])