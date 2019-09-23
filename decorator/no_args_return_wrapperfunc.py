# -*- coding: utf-8 -*-

def args_logger(f):
    def wrapper(*args, **kwargs):
        f(*args, **kwargs)
        print('args: {}, kwargs: {}'.format(args, kwargs))
    return wrapper


@args_logger
def print_message(msg):
    print(msg)

# 以下と等価
'''
def print_message(msg):
    print(msg)
print_message = args_logger(print_message)
'''

print_message('hello')

# output:
# hello
# args: ('hello',), kwargs: {}
