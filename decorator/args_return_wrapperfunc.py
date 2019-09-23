# -*- coding: utf-8 -*-


def args_joiner(*dargs, **dkwargs):
    def decorator(f):
        def wrapper(*args, **kwargs):
            newargs = dargs + args  # リストの結合
            newkwargs = {**kwargs, **dkwargs}   # 辞書の結合
            f(*newargs, **newkwargs)
        return wrapper
    return decorator


@args_joiner('darg', dkwarg=True)
def print_args(*args, **kwargs):
    print('args: {}, kwargs: {}'.format(args, kwargs))

# 以下と等価
'''
def print_args(*args, **kwargs):
    print('args: {}, kwargs: {}'.format(args, kwargs))
print_args = args_joiner('darg', dkwarg=True)(print_args)
'''

print_args('arg', kwarg=False)

# output:
# args: ('darg', 'arg'), kwargs: {'kwarg': False, 'dkwarg': True}
