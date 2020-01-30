#!/usr/bin/env python
# coding=utf-8


class Base(object):
    class_var = 1       # 类变量

    def foo(self, x):
        self.class_var = x  # 绑定实例，覆盖类变量


if __name__ == "__main__":
    b = Base()
    b1 = Base()
    print(Base.class_var, b.class_var, b1.class_var)        # 同一个引用
    print(Base.class_var is b.class_var, b.class_var is b1.class_var)

    b.foo(100)
    print(Base.class_var, b.class_var, b1.class_var)        # 不同一个引用
    print(Base.class_var is b.class_var, b.class_var is b1.class_var)
    print(b.__dict__, b1.__dict__, Base.__dict__, sep=", ")
    print(dir(b) == dir(Base))

    del b.class_var     # 删除类型实例，覆盖消除。p3中变量的解析路径相关
    print(Base.class_var, b.class_var, b1.class_var)  # 同一个引用
    print(Base.class_var is b.class_var, b.class_var is b1.class_var)

    b.class_var = 1000  # 实例引用赋值也会导致实例参数绑定，隐藏类变量
    print(Base.class_var, b.class_var, b1.class_var)  # 同一个引用
    print(Base.class_var is b.class_var, b.class_var is b1.class_var)
