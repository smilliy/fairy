# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-


import requests
from requests.auth import HTTPBasicAuth
import json
import re
from ReadSpecToXls import ReadSpecToXls
from PrintJson import PrintJson


def basic_auth(ip, uri, user_id, password, method, headers, body, spec_file, result_file):
    if method == 'Get':
        request_for_url = requests.get(ip+uri, auth=HTTPBasicAuth(user_id, password), verify=False)
    elif method == 'Post':
        request_for_url = requests.post(ip+uri, json=eval(body), auth=HTTPBasicAuth(user_id, password), verify=False)
        pass
    elif method == 'Patch':
        request_for_url2 = requests.get(ip + uri, auth=HTTPBasicAuth(user_id, password), verify=False)
        etag = ''
        for i in request_for_url2.headers:
            if str(i).upper() == 'ETAG':
                etag = request_for_url2.headers[i]
        headers = {"If-Match": "%s" % etag}
        request_for_url = requests.patch(url=ip+uri, json=eval(body), headers=headers, auth=HTTPBasicAuth(user_id, password), verify=False)
        pass
    elif method == 'Delete':
        request_for_url = requests.delete(ip + uri, auth=HTTPBasicAuth(user_id, password), verify=False)
        pass
    test_headers = ''
    for j in request_for_url.headers:
        test_headers += j + ' : ' + request_for_url.headers[j] + '\n'
    request_for_url_to_json = json.loads(request_for_url.text)
    request_for_url_to_json_output = json.dumps(request_for_url_to_json)
    n = re.sub('\: null', ': "null"', re.sub('\: true', ': "true"', re.sub('\: false', ': "false"', request_for_url_to_json_output)))
    a = PrintJson()
    a.set_json(eval(n))
    t = ReadSpecToXls(spec_file, result_file,'[Status: ' + str(request_for_url.status_code) + '] [' + method + ' ' +ip + uri + ']', test_headers, test_body=json.dumps(json.loads(request_for_url.text), indent=4), test_result=a.get_json())
    t.write_result_to_spec()


if __name__ == '__main__':
    import os
    r1 = requests.get('https://10.245.16.250/redfish/v1/Systems/1/Oem/Lenovo/Metrics/MemorySubsystemPower/', auth=HTTPBasicAuth('USERID', 'PASSW0RD'), verify=False)

    # print r.text
    # print r.content
    # (ip, uri, userid, password, auth, method)

    f1 = json.loads(r1.text)

    t = json.dumps(f1, indent=4)

    # print t
    # print type(t)

    m1 = json.dumps(f1)
    n1 = re.sub('\: null', ': "null"', re.sub('\: true', ': "true"', re.sub('\: false', ': "false"', m1)))

    a1 = PrintJson()
    a1.set_json(eval(n1))
    aaa = ''
    for i in r1.headers:
        aaa += i + ' : ' + r1.headers[i] + '\n'
    print r'%s' % aaa
    print '++++++++'
    print a1.get_json()
    print t

    # print json.dumps(json.loads(str(r1.headers)), indent=4)


    t1 = ReadSpecToXls('test.xlsx', 'Result.xlsx', '10.245.16.25000', aaa, t, a1.get_json())

    t1.write_result_to_spec()
