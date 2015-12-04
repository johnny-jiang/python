import os, stat
from sys import argv
from pwd import getpwuid
from grp import getgrgid
from time import ctime



def dir():
    all_stat = []
    error_stat = []
    total=0
    for filename in os.listdir('.'):
        try:
            st_result = os.lstat(filename)
            mode = stat.filemode(st_result.st_mode)
            nlink = str(st_result.st_nlink)
            owner = getpwuid(st_result.st_uid)[0]
            group = getgrgid(st_result.st_gid)[0]
            size = str(st_result.st_size)
            total += st_result.st_size
            time = ctime(st_result.st_mtime)[4:16]
            all_stat.append(' '.join([mode, nlink, owner, group, size, time, filename]))
        except FileNotFoundError:
            error_stat.append("ls: cannot access aa: No such file or directory: %s" % filename)
            continue

    for er in error_stat:
        print(er)
    print('total ',str(total))
    for file_stat in all_stat:
        print(file_stat)

if __name__ == '__main__':
    dir()