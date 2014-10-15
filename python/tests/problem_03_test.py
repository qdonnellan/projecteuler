from problems.problems_01_25.problem_03 import largest_prime_factor
import unittest

class Problem03Test(unittest.TestCase):
    """
    test the implementation of Project Euler Problem 03
    """

    def test_case_where_n_equals_10(self):
        """
        the largest prime factor of 10 is 5
        """
        self.assertEqual(largest_prime_factor(10), 5)

    def test_case_where_n_equals_13195(self):
        """
        the largest prime factor of 13195 is 29
        """
        self.assertEqual(largest_prime_factor(13195),29)
