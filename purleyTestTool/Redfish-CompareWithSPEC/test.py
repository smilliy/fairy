# -*- coding: utf-8 -*-


import requests
from requests.auth import HTTPBasicAuth
import json

from ReadSpecToXls import ReadSpecToXls
from PrintJson import PrintJson

import re

r = requests.get('https://10.245.17.154/redfish/v1/AccountService/', auth=HTTPBasicAuth('USERID', 'PASSW0RD'), verify=False)

# print r.text
# print r.content

f = json.loads(r.text)

# t = json.dumps(f, indent=4)
# print t
# print type(t)

m = json.dumps(f)

n = re.sub('\: null', ': "null"', re.sub('\: true', ': "true"', re.sub('\: false', ': "false"', m)))

a = PrintJson()
a.set_json(eval(n))


t = ReadSpecToXls('spec.xls', a.get_json())

t.write_result_to_spec()
