def f(x):
    if x == 0:
        return 0
    return x - f(f(x-1))


def g(x):
    if x == 0:
        return 0
    return x - f(x-1)


def q(x):
    if x == 0:
        return 0
    return x - q(q(q(x - 1)))


if __name__ == '__main__':
    for x in range(20):
        print (x, g(x), f(x), q(x))  # code to be executed

    for x in range(20):
        print(x, g(x), f(g(x)), q(f(g(x))))  # code to be executed
