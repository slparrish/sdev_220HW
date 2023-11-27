# test_sum_2.py Parrish, Scott 11/25/2023 V: 0.2
# file to test the default sum function via assert.  This file incorporates
# the test_sum.py file and adds the test_sum_tuple() test function. This
# test can also be run using the pytest module and nose2

def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"


def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"


if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    print("Everything passed")


"""
 $ python3 test_sum_2.py
Traceback (most recent call last):
  File "/home/scott/Documents/School/sdev_220/playground/sdev_220HW/ParrishScott_M05_UnitTests/test_sum_2.py", line 11, in <module>
    test_sum_tuple()
  File "/home/scott/Documents/School/sdev_220/playground/sdev_220HW/ParrishScott_M05_UnitTests/test_sum_2.py", line 6, in test_sum_tuple
    assert sum((1, 2, 2)) == 6, "Should be 6"
AssertionError: Should be 6

"""