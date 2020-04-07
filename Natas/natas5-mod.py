#!/usr/bin/env python3

import requests
import re

username = 'natas5'
password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'

# headers = { "Referer" : "http://natas5.natas.labs.overthewire.org/" }

url = 'http://%s.natas.labs.overthewire.org/' % username

response = requests.get(url, auth = (username, password))
content = response.text
cookies = response.cookies

print(content)
# for c in response.cookies:
#     print(c.name, c.value)

print(cookies)

# print(re.findall('natas4:(.*)', content)[0]))