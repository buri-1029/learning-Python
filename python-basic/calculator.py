# function version
def plus(a, b):
    if type(a) is str or type(b) is str:
        return None
    else:
        return a + b
    # return int(a) + int(b)


def minus(a, b):
    if (int(b) > int(a)):
        return int(b) - int(a)
    return int(a) - int(b)


def times(a, b):
    return int(a) * int(b)


def division(a, b):
    return int(a) // int(b)


def negation(a):
    return -int(a)


def power(a, b):
    return int(a) ** int(b)


def remainder(a, b):
    return int(a) % int(b)


print(plus(2, "4"))
print(minus(2, "4"))
print(times(2, "4"))
print(division("4", 2))
print(negation(2))
print(power(2, "4"))
print(remainder(2, "4"))
