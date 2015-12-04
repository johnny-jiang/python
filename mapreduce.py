# 练习
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：


# -*- coding: utf-8 -*-

def normalize(name):
    return str.upper(name[0])+str.lower(name[1:])


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)




# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：

# -*- coding: utf-8 -*-

from functools import reduce

def prod(L):
    def multiply(a,b):
        return a*b
    return reduce(multiply,L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))



# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
# -*- coding: utf-8 -*-

from functools import reduce

def str2float(s):
    flag=10
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':'.'}[s]
    def fn(a,b):
        nonlocal flag
        if b=='.' :
            flag=1
            return a
        if flag<2 :
            flag=flag*0.1
            return a+b*flag
        else:
            return a*10+b
    return reduce(fn, map(char2num, s))


print('str2float(\'123.456\') =', str2float('123.456'))

