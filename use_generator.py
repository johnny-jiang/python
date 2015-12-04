#use_generator.py
# -*- coding: utf-8 -*-

def triangles():

    new=[]
    old=[1]
    while True:
        yield old
        old.append(1)
        new.append(1)
        for i in range(1,len(old)-1):
            new.append(old[i-1]+old[i])
        new.append(1)
        old=new
        new=[]


            

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break