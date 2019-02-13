#!/usr/bin/env python
import string


def generate_letters():
    for letter in 'abc':
        yield letter


def alphabet_cycle():
    while True:
        for c in string.lowercase:
            yield c


q = zip('lorem ipsum', alphabet_cycle())

print(q)


def alpha_numeric_cycle():
    n = 1
    while True:
        for c in 'abcdefghijklmnopqrstuvwxyz':
            yield "%s%d" % (c, n)
        n = n + 1


iter = alpha_numeric_cycle()

for i in range(200):
    print(iter.next())
