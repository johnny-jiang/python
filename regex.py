# regex.py
import re
re_email=re.compile(r'(\w+)@(\w+).(\w+)')
print('email: asf@sdf.cc.cn')
print(re_email.match('asf@sdf.cc.cn').groups())
re_email2=re.compile(r'<([0-9a-zA-Z ]+)>\s*(\w+)@([0-9a-zA-Z.]+)')
print('email: <abc> asdf@sdf.cc.cc')
print(re_email2.match('<abc> asdf@sdf.cc.cc').groups())