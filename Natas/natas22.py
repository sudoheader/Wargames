#!/usr/bin/env python3

import requests
import re
import binascii

username = 'natas22'
password = 'chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ'

url = 'http://%s.natas.labs.overthewire.org/' % username
experimenter = 'http://natas21-experimenter.natas.labs.overthewire.org/?debug=true&submit=1&admin=1'

session = requests.Session()

response = session.get(url, auth = (username, password))
# response = session.post(experimenter, auth = (username, password))
# print(response.text)
# old_session = session.cookies["PHPSESSID"]

# response = session.get(url, cookies = { "PHPSESSID": old_session }, auth = (username, password))
print(response.text)
# print(re.findall('Password: (.*)</pre>', response.text)[0])