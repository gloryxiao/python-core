#!/usr/bin/env python
# coding=utf-8


def fab(n):
    x, y = 1, 1
    step = 1
    while step <= n:
        yield x
        tmp = x
        x = y
        y += tmp
        step += 1


if __name__ == "__main__":
    f = fab(10)
    print f
    for item in f:
        print item

    f1 = (x+1 for x in xrange(100))
    print f1
    f2 = xrange(10)
    print f2

