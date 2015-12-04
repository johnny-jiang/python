#use_hashlib.py
import hashlib

db = {}

def get_md5(s):
    sha1=hashlib.md5()
    sha1.update(s.encode('utf-8'))
    return sha1.hexdigest()

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')

def login(username, password):
    return db[username]==get_md5(password + username + 'the-Salt')


register('abc','aaa')
assert login('abc','aaa') == True
assert login('abc','bbb') == False
print('pass')