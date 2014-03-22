from problems_01_25.problem_07 import nth_prime
import unittest

class Problem07Test(unittest.TestCase):
    """
    test the implementation of Project Euler Problem 7
    """
    def test_for_first_prime(self):
        """
        the first prime number is 2
        """
        self.assertEqual(nth_prime(1), 2)

    def test_for_third_prime(self):
        """
        the third prime number is 5
        2, 3, [5]
        """
        self.assertEqual(nth_prime(3), 5)

    def test_for_sixth_prime(self):
        """
        the sixth prime number is 13
        2, 3, 5, 7, 11, [13]
        """
        self.assertEqual(nth_prime(6), 13)

    def test_for_10th_prime(self):
        """
        the 10th prime number is 29
        2, 3, 5, 7, 11, 13, 17, 19, 23, [29]
        """
        self.assertEqual(nth_prime(10), 29)
