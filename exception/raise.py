
def raise_func(id_str: str)-> bool:
    res = ""
    if id_str == "0":
        res = "配信可能"
    elif id_str == "1":
        res = "配信不可"
    else:
        e = Exception("aaa")
        print(e.args)
        raise e
    print("???")
    return res


def raise_func2():
    raise Exception("ccc")
    print("このprintは実行されない")

print(raise_func("0"))
print(raise_func("1"))

# raiseするときは以降は実行されない
try:
    print(raise_func("2"))
except Exception as e:
    print(str(e.args))

try:
    raise Exception("bbb")
except Exception as e:
    print(e)

try:
    raise_func2()
except:
    print("ddd")
