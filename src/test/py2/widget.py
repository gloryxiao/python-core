#!/usr/bin/env python
# coding=utf-8


class Widget(object):
    def __init__(self, title):
        print("init called")
        self.title = title
        self._w = 0
        self._h = 0

    def size(self):
        return self._w, self._h

    def resize(self, w=0, h=0):
        self._w = w
        self._h = h

    def dispose(self):
        print("dispose called")
        self._w = 0
        self._h = 0
