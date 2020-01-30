#!/usr/bin/env python
# coding=utf-8


# py3的元类声明不同于py2，在类声明时使用metaclass来绑定。元类一样继承type类型，元类的方法绑定参数是cls，除了__new__(cls, *args, **kw)
# 中cls为元类类型外，其他方法参数（如__init__(cls, *args, **kw)）中cls全部绑定声明的类类型
class Meta(type):
    def __new__(cls, name, bases, dicts):
        # 编译解释函数，生成类型信息
        print("in meta __new__, cls is: ", cls, ", name: ", name, ", bases: ", bases, ", dicts: ", dicts)
        x = super().__new__(cls, name, bases, dicts)
        return x

    def __init__(cls, name, bases, dicts):
        # 编译解释函数
        print("in meta __init__, cls is: ", cls, ", name: ", name, ", bases: ", bases, ", dicts: ", dicts)
        super().__init__(name, bases, dicts)

    def __call__(self, *args, **kwargs):
        # 运行时函数
        print("in meta __call__, self is: ", self)
        return super().__call__(*args, **kwargs)


class Foo(metaclass=Meta):
    pass


if __name__ == "__main__":
    print("###### runtime... ")
    f = Foo()
    print("f:", f)
