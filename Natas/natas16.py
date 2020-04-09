#!/usr/bin/env python3

import requests
import re
import urllib
import base64
import binascii
from string import *

characters = ascii_lowercase + ascii_uppercase + digits

username = 'natas16'
password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
# blind sql injection

response = requests.get(url, auth = (username, password))
# response = session.get(url + "upload/uyqhobeodo.php?c=cat /etc/natas_webpass/natas14", auth = (username, password))

content = response.text

print(content)

# print(re.findall('natas15 is (.*)<br>', content)[0])