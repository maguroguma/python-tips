# -*- coding: utf-8 -*-


def can_cast_to_float(s: str):
    try:
        float(s)
    except:
        return False
    return True


def can_cast_to_integer(s: str):
    try:
        int(s)
    except:
        return False
    return True

f_str = '111.111'
i_str = '222'
s_str = ''

print(can_cast_to_float(f_str))   # True
print(can_cast_to_float(i_str))   # True
print(can_cast_to_float(s_str))   # False
print(can_cast_to_integer(f_str)) # False
print(can_cast_to_integer(i_str)) # True
print(can_cast_to_integer(s_str)) # False

print("---")
l = ['1', '2.2', '3']
for s in l:
    try:
        print(int(s))
    except:
        print("not int string")
