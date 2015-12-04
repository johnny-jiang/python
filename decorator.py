#请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。


import functools

def begincall(func):
    def wrapper(*args, **kw):
        print("begin call")
        return func(*args, **kw)
    return wrapper


def endcall(func):
    def wrapper(*args, **kw):
        f=func(*args, **kw)
        print("end call")
        return f
    return wrapper


@begincall
@endcall
def f():
	print(1234)


f()

#再思考一下能否写出一个@log的decorator，使它既支持：

#@log
#def f():
#    pass
#又支持：

#@log('execute')
#def f():
#    pass


import functools


def log(text='execute'):
    def begincall(func):
        def wrapper(*args, **kw):
            print("%s  %s" % (text,func.__name__))
            return func(*args, **kw)
        return wrapper
    return begincall



@log()
def f():
	print(12344)


f()



@log('ess')
def g():
	print(12344)


g()
