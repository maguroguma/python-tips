# -*- coding: utf-8 -*-

from functools import wraps


def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print('^^^^^^^^^^^^^^')
        # return f(*args, **kwds)
        f(*args, **kwds)
        print('vvvvvvvvvvvvvv')
    return wrapper


@my_decorator
def example(i: int, s: str):
    """ example docstring """
    print('Called example function')
    print('int argument: {}, str argument: {}'.format(i, s))
    print('Over example function')


example(100, 'Hello')
# wrapsのおかげで関数名とdocstringが維持される
print(example.__name__)
print(example.__doc__)

