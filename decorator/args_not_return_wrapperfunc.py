# -*- coding: utf-8 -*-


funcs = []
def appender(*args, **kwargs):
    def decorator(f):
        # argsやkwargsの内容によって処理内容を変えたり変えなかったり
        print(args)
        print(kwargs)
        if kwargs.get('option1'):
            print('option1 is True')

        # 元の関数をfuncsに追加
        funcs.append(f)
    return decorator


@appender('arg1', option1=True)
def hoge():
    print('hoge')


@appender('arg2', option2=False)
def fuga():
    print('fuga')

# 以下と等価
'''
def hoge():
    print('hoge')
appender('arg1', option1=True)(hoge)

def fuga():
    print('fuga')
appender('arg2', option2=False)(fuga)
'''

for f in funcs:
    f()

# output:
# ('arg1',)
# {'option1': True}
# option1 is True
# ('arg2',)
# {'option2': False}
# hoge
# fuga
