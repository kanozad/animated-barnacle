﻿def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fib()

for i in range(20):
    print f.next(),
