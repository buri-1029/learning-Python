def test(a, b, *args, **kwargs):
    print(args)
    print(kwargs)
    return a + b


plus(1, 2, 1, 1, 1, 1, aa=True, bb=True, cc=True)


def plus(*args):
    result = 0
    for num in args:
        result += num
    print(result)


plus(1, 2, 1, 2, 3, 4, 5)
