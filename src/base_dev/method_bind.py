#!/usr/bin/env python
# coding=utf-8


def foo(x, y):
    print x, y


class Bar(object):
    def bar(self, x):
        print "execute bar, self: %s, x: %s" % (self, x)

    @classmethod
    def class_bar(cls, x):
        print "execute class_bar, cls: %s, x: %s" % (cls, x)

    @staticmethod
    def static_bar(x):
        print "execute static bar, x: %s" % x


class SubBar(Bar):
    pass


if __name__ == "__main__":
    b = Bar()
    print "foo:", foo
    foo(b, 1)
    print "b.bar", b.bar
    b.bar(1)
    print "b.class_bar", b.class_bar
    b.class_bar("aaa")
    print "b.static_bar", b.static_bar
    b.static_bar(2)

    print "Bar.bar", Bar.bar
    Bar.bar(b, 1)
    print "Bar.class_bar", Bar.class_bar
    Bar.class_bar(1)
    print "Bar.static_bar", Bar.static_bar
    Bar.static_bar("hah")

    print "Bar.class_bar:", Bar.class_bar, ", id:", id(Bar.class_bar)
    Bar.class_bar(1)
    print "SubBar.class_bar", SubBar.class_bar, ", id:", id(SubBar.class_bar)
    SubBar.class_bar(2)
