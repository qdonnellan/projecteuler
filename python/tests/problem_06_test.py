from problems.problems_01_25.problem_06 import sum_squared_less_squared_sum
import unittest

class Problem06Test(unittest.TestCase):
    """
    test the implementation of Project Euler Problem 6
    """

    def test_first_ten_ints(self):
        """
        the square of the first 10 ints' sum is:
        (1 + 2 + ... + 10)^2 = 552 = 3025

        the sum of the square of first 10 ints is:
        1^2 + 2^2 + ... + 10^2 = 385

        thus, the difference should be 3025-385 = 2640
        """
        self.assertEqual(sum_squared_less_squared_sum(10), 2640)
