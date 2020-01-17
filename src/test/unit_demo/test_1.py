#!/usr/bin/env python
# coding=utf-8

import unittest


def testSomething():
    """
    assume this is old test function
    :return:
    """
    something = dict()
    assert something.name is not None


def setup():
    print "setup"


def teardown():
    print 'teardown'


# one can create an equivalent test case instance as follows, with optional set-up and tear-down methods:
testcase = unittest.FunctionTestCase(testSomething,
                                     setUp=setup,
                                     tearDown=teardown)

if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(testcase)
    import test_suites
    suite.addTest(test_suites.suite())

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
