#!/usr/bin/env python
# coding=utf-8

import unittest
from test_file1 import WidgetTestCase
from test_unittest import TestStringMethods


def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_widget_resize'))
    suite.addTest(TestStringMethods("test_isupper"))
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
