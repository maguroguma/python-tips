
def run():
    for i in range(0, 10):
        try:
            if i % 2 == 0:
                print(i)
            else:
                raise Exception("ODD NUMBER!")
            print("try DONE")
        except Exception as e:
            print(e)
    for i in range(0, 10):
        try:
            if i % 2 == 0:
                raise Exception("EVEN NUMBER!")
            else:
                print(i)
            print("try DONE")
        except Exception as e:
            print(e)

    try:
        raise Exception('First Exception')
    except Exception as e:
        print(e)
        raise Exception('Second Exception')


def nest():
    try:
        raise Exception("OUT")
    except Exception as e:
        try:
            print(e)
            raise Exception("IN")
            print("実行されない")
        except Exception as ee:
            print(ee)


def code_block():
    try:
        inner1 = 100
        raise Exception("tekitou")
        inner2 = 200
    except:
        pass
    print(inner1)
    print(inner2)   # これは参照できない


def one_except():
    try:
        1/0
    except ZeroDivisionError as ze:
        # print(ze)
        pass
    except Exception as e:
        print('not printed.')

# try:
#     run()
# except Exception as e:
#     print(e)

# nest()

# Pythonはブロックスコープはない
# code_block()

one_except()
