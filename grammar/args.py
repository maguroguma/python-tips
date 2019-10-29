# -*- coding: utf-8 -*-

def many_arguments(a, b, c, d, e):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)


many_arguments(1, 2, 3, 4, 5)
many_arguments(e=5, d=4, c=3, b=2, a=1)
many_arguments(e=1, d=2, c=3, b=4, a=5)
