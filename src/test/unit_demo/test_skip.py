#!/usr/bin/env python
# coding=utf-8

import sys
import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print "setUp"

    def tearDown(self):
        print "tearDown"

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(sys.version_info < (1, 3),
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

    def test_maybe_skipped(self):
        if not False:
            self.skipTest("external resource not available")
        # test code that depends on the external resource
        pass


@unittest.skip("showing class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass


class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")

# new in 3.4
# class NumberTest(unittest.TestCase):
#     def test_even(self):
#         for i in range(6):
#             with self.subTest(i=i):
#                 self.assertEqual(i % 2, 0)

