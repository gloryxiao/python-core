#!/usr/bin/env python
# coding=utf-8
"""
使用简单的pytest单测
"""


def inc(x):
    return x + 1


def test_inc():
    assert inc(3) == 5
