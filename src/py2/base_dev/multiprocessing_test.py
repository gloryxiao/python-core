# coding=utf-8

from multiprocessing.dummy import Pool


def f(x):
    return x*x


def callback(arg):
    print "hello, %s" % arg


if __name__ == "__main__":
    pool = Pool(processes=4)
    res = pool.apply_async(f, (10,), callback=callback)
    print res.get(timeout=1)

