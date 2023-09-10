def log(fun):
    # wrap 增强函数，用于增强被装饰的函数
    def wrap(*args, **kwargs):
        # 调用被封装的函数
        r = fun(*args, **kwargs)
        print(f"{r} = fun({args} {kwargs})")
        return r

    # 返回的函数本身，而不是函数的调用结果
    return wrap


def test_recur():
    r = fac(4)
    print(r)
    assert r == 24


@log
def fac(n):
    if n == 1:
        return 1
    else:
        r = n * fac(n - 1)
        return r
