#!/usr/bin/env python
# coding=utf-8


class A(object):
    def __init__(self):
        self._vi = "do"             # protect attribute
        self.__private = "pri"      # private attribute  ==> _A__private
        
    def __getattribute__(self, name):
        return super(A, self).__getattribute__(name)
        # return self.__dict__[name]                                  # Error dead loop
        # return object.__getattribute__(self, name)
        # return super(self.__class__, self).__getattribute__(name)   # Error dead loop self.__class__ hacked!


if __name__ == "__main__":
    a = A()
    print a._vi
    print a.__dict__
    print a._A__private


