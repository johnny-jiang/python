#do_base64.py
# -*- coding: utf-8 -*-

import base64

def safe_base64_decode(s):
    a = (-len(s)) % 4
    if isinstance(s,str):
        s=s+'='*a
        return base64.b64decode(s.encode('utf-8'))
    else:	
        s=s+b'='*a
        return base64.b64decode(s)


# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')