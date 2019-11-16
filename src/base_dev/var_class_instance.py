#!/usr/bin/env python
# coding=utf-8


class Person(object):
    name = "person"
    test = []
    test1 = []


class Teacher(Person):
    name = "teacher"
    test = []


if __name__ == "__main__":
    print Person.name
    p1 = Person()
    p2 = Person()
    p1.name = "sean"
    print "p1.name:", p1.name, ", id(p1.name), ", id(p1.name)
    print "p2.name:", p2.name, ", id(p2.name), ", id(p2.name)
    print "Person.__dict__:", Person.__dict__, ", id(Person.name): ", id(Person.name)
    print "Teacher.__dict__:", Teacher.__dict__, ", id(Teacher.name)", id(Teacher.name)
    t = Teacher()
    # print Person(t).name      # 似乎没有向上转型这一说, 只有一些内置的转型函数
    print "id(Teacher.test)", id(Teacher.test)
    print "id(Person.test)", id(Person.test)
    print "id(Teacher.test1)", id(Teacher.test1)
    print "id(Person.test1)", id(Person.test1)
    t.test.append(1)
    t.test1.append("a")

    print p1.test
    print p1.test1
    print Teacher.test


