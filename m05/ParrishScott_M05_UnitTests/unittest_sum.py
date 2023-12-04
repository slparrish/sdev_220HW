# unittest_sum.py  Parrish, Scott 11/25/23 V: 0.1 
# Test the built-in sum() function using the unit tests built on the built-in
# unittest library utilizing a TestSum class with 2 methods, one that tests
# sum() with a list of 3 numbers and another that tests the function using
# a tuple of 3 numbers (that do not add up to the expected result) producing 
# one success and a failure.  These tests can also be run using nose2 and 
# pytest.

import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")


if __name__ == "__main__":
    unittest.main()


"""
$ python3 -m unittest_sum
.F
======================================================================
FAIL: test_sum_tuple (__main__.TestSum.test_sum_tuple)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/scott/Documents/School/sdev_220/playground/sdev_220HW/ParrishScott_M05_UnitTests/unittest_sum.py", line 10, in test_sum_tuple
    self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
AssertionError: 5 != 6 : Should be 6

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
"""