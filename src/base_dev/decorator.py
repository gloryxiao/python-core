#!/usr/bin/env python
# coding=utf-8

import functools

"""
Decorating methods
One nifty thing about Python is that methods and functions are really the same. The only difference is that methods
expect that their first argument is a reference to the current object (self).

That means you can build a decorator for methods the same way! Just remember to take self into consideration:
"""


def decorate_method(func):
    def wrapper(self, a):
        a += "big"
        func(self, a)

    return wrapper


'''
Best practices: decorators
Decorators were introduced in Python 2.4, so be sure your code will be run on >= 2.4.
Decorators slow down the function call. Keep that in mind.
You cannot un-decorate a function. (There are hacks to create decorators that can be removed, but nobody uses them.)
 So once a function is decorated, it’s decorated for all the code.
Decorators wrap functions, which can make them hard to debug. (This gets better from Python >= 2.5; see below.)
The functools module was introduced in Python 2.5. It includes the function functools.wraps(), which copies the name, 
module, and docstring of the decorated function to its wrapper.

(Fun fact: functools.wraps() is a decorator! ☺)
'''


def best_wrapper(func):
    @functools.wraps(func)
    def wrapper(self, x):
        x += ", best big"
        func(self, x)

    return wrapper


class Cat(object):
    @decorate_method
    def mao(self, x):
        print x

    @best_wrapper
    def best_mao(self, x):
        print x


if __name__ == "__main__":
    cat = Cat()
    print cat.mao
    cat.mao("miao ")
    print cat.best_mao
    cat.best_mao("miao ")
