import os
import sys
import random
from functools import reduce


def main(args):
    random.seed = (os.urandom(1024))

    for x in range(30):
        r = roll(random.randint(6, 8))
        t = random.randint(1, 4)
        print(
            r, hits(r), total(r), is_glitch(r), is_critical_glitch(r), is_success(
                r, t), ("(%s)" %
                        t), margin_of_success(
                r, t))
        if count(6, r) != 0:
            print("rule of six: ", rule_of_six(r))

    r = [1, 1, 1, 2, 3, 4, 1]
    print(r, hits(r), is_glitch(r), is_critical_glitch(r))

    r = [1, 1, 1, 2, 3, 5, 1]
    print(r, hits(r), is_glitch(r), is_critical_glitch(r))

    for i in range(1, 13):
        sumo = [0, 0, 0, 0, 0, 0]
        for j in range(10000):
            for k in range(6):
                if is_success(roll(i), k + 1):
                    sumo[k] += 1
        print(i, sumo)


def roll(n, d=6):
    """

    :param n: number of dice to roll
    :param d: number of sides per die
    :param bonus:
    :return:
    """
    return [random.randint(1, d) for i in range(n)]


def total(r, bonus=0):
    """

    :param r:
    :param bonus:
    :return:
    """
    return reduce(lambda q, p: p + q, r) + bonus


def rule_of_six(r):
    """

    :param r:
    :return:
    """
    i = count(6, r)
    res = list(r)  # copy the original list

    while i != 0:
        tmp = roll(i)
        res.extend(tmp)
        i = count(6, tmp)

    return res


def margin_of_success(r, t):
    """

    :param r:
    :param t:
    :return:
    """
    return hits(r) - t


def is_success(r, t):
    """

    :param r:
    :param t:
    :return:
    """
    return hits(r) >= t


def is_hit(n):
    """

    :param n:
    :return:
    """
    if n > 4:
        return 1
    return 0


def count(n, r):
    """

    :param n:
    :param r:
    :return:
    """
    res = [x for x in r if x == n]
    return len(res)


def is_glitch(r):
    """

    :param r:
    :return:
    """
    return count(1, r) / len(r) >= 0.5


def is_critical_glitch(r):
    """

    :param r:
    :return:
    """
    return is_glitch(r) and hits(r) == 0


def hits(r):
    """

    :param r:
    :return:
    """
    res = [x for x in r if is_hit(x)]
    return len(res)


if __name__ == '__main__':
    main(sys.argv[1:])
