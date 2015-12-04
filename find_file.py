import os,sys
if len(sys.argv) < 2:
    print("useage:\python script_name.py find_str")
    sys.exit()
find_str = sys.argv[1]

def findfile(name,path='.'):
    print('path : %s'%path)
    pwd = os.path.abspath(path)
    print(os.listdir(pwd))
    for f in os.listdir(pwd):
        if os.path.isdir(f):
            findfile(name,f)
        if os.path.isfile(f) and (name in os.path.split(f)[1]):
            print('The file in:')
            print(os.path.join(pwd,f))

findfile(sys.argv[1])
