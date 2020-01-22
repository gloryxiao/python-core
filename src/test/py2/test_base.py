#!/usr/bin/env python
# coding=utf-8
"""
使用简单的pytest单测
"""

import pytest


def inc(x):
    return x + 1


def test_inc():
    assert inc(3) == 5


def func_exception():
    raise SystemExit(1)


def test_exception():
    with pytest.raises(SystemExit) as exec_info:
        func_exception()

    assert exec_info.type == SystemExit


class TestClass(object):
    # def __init__(self):  # 不包含__init__，否则不收集test条目
    #     pass

    def test_one(self):
        h = "this"
        assert 'h' in h
