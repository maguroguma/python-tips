# デコレータの練習

[Pythonデコレータ再入門〜デコレータは種類別に覚えよう〜](https://qiita.com/macinjoke/items/1be6cf0f1f238b5ba01b)の写経。

## デコレータ関数の種類分け

- 引数を取るか否か
- ラッパー関数を返すか否か

### 1. 引数なしデコレータでラッパー関数を返す場合

```python
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
```

一番理解しやすい形。

ラッパー関数を返す（ので、デコレータ関数が返す関数の名前は `wrapper` とするのが慣例）。

### 2. 引数ありデコレータでラッパー関数を返さない場合

```python
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
```

`appender` デコレータは元の関数を `funcs` リストにappendする。
デコレータ関数に渡された引数によって処理内容を変えたりできる。

注意する点は、デコレータに引数を保つ場合、 **デコレータ関数内では直接元の関数 `f` を扱えないということ。**
**代わりに「元の関数を扱う関数」を定義する。**
この関数名は慣例として `decorator` という名前をつける。

※このパターンのデコレータとしては flask の `app/Flask.route` 関数が当てはまる。

※flaskのように、単にコールバック関数を定義するためにこのパターンは使われると思われる。

#### 個人的メモ

```python
# 以下と等価
'''
def hoge():
    print('hoge')
appender('arg1', option1=True)(hoge)

def fuga():
    print('fuga')
appender('arg2', option2=False)(fuga)
'''
```

`appender('arg1', option1=True)` の部分によって、 `decorator` 関数オブジェクトがreturnされる。
返された `decorator` によって `decorator(hoge)` のように（この例では） `hoge` 関数が登録される。

よって、 `wrapper` 関数というものは登場していない。

### 3. 引数ありデコレータでラッパー関数を返す場合

```python
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
```

1番目の例と2番目の例の合せ技（よってデコレータ関数内のネストがさらに1段深くなっている）。

「【関数を返す関数】を返す」という形。

#### 個人的メモ

**最初2つの例を強く頭になじませることができれば、3番目も自然と理解できると思う。**

---

## どの種類のデコレータなのか見抜けるようになろう

3つの例を通してまとめ。
デコレータが何をしているか理解するために、どの種類のデコレータなのかを見抜ければ後は楽である。

※実用上、見かけからパターンマッチがスムーズにできるようになれば、プログラムも読みやすくなると思うので、強く意識したい。

### 1つ目

```python
def hoge_deco(func):
    def wrapper(...):
        ...
    return wrapper
```

判断ポイントは、 **`hoge_deco` の引数に `func` を撮っていることと、 `wrapper` 関数を定義してそれを最後にreturnしているところ。**

### 2つ目

```python
def fuga_deco(*args, **kwargs):
    def decorator(func):
        # args, kwargs, funcを使ってなにかする（funcをあるリストに加えるなど）
        ...
    return decorator
```

判断ポイントは、 **`fuga_deco` の引数に関数以外の何かを撮っていることと、 `wrapper` という名前ではなく、関数 `func` を引数に取る `decorator` という名前の関数が定義されていてそれを返していること。**

**このパターンのデコレータはラッパー関数を返さないので元の関数自体はなんの変化もないことに注意。**

### 3つ目

```python
def piyo_deco(*dargs, **dkwargs):
    def decorator(f):
        ...
        def wrapper(*args, **kwargs):
            ...
        return wrapper
    return decorator
```

