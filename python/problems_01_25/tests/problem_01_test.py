from problems_01_25.problem_01 import sum_three_five
import unittest

class Problem01Test(unittest.TestCase):
    """
    test the implementation of problem one
    """

    def test_numbers_less_than_equal_to_ten(self):
        """
        test problem1 case where limit is 10

        there are 4 multiples of 3 or 5 less than 10,
        their sum is 23
        """
        self.assertEqual(sum_three_five(10),23)
