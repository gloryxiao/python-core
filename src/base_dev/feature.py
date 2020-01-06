#!/usr/bin/env python
# coding=utf-8

"""
2.3.2 __new__静态方法
新式类都有一个__new__的静态方法，它的原型是object.__new__(cls[, ...])
cls是一个类对象，当你调用C(*args, **kargs)来创建一个类C的实例时，python的内部调用是
C.__new__(C, *args, **kargs)，然后返回值是类C的实例c，在确认
c是C的实例后，python再调用C.__init__(c, *args, **kargs)来初始化实例c。

object.__new__()创建的是一个新的，没有经过初始化的实例。当你重写__new__方法时，可以不
用使用装饰符@staticmethod指明它是静态函数，解释器会自动判断这个方法为静态方法。如果
需要重新绑定C.__new__方法时，只要在类外面执行C.__new__ = staticmethod(yourfunc)就可以了
"""


class Singleton(object):
    _singleton = {}

    def __new__(cls, *args, **kwargs):
        print cls
        if not cls._singleton.get(cls):
            cls._singleton[cls] = super(Singleton, cls).__new__(cls)
        return cls._singleton[cls]

    def __init__(self):
        print "init " + self.__class__.__name__


if __name__ == "__main__":
    s1 = Singleton()
    print s1
    s2 = Singleton()
    print s2
