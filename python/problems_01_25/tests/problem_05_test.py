from problems_01_25.problem_05 import natural_num_division_streak
import unittest

class Problem05Test(unittest.TestCase):
    """
    test the implementation of Project Euler Problem 05
    """

    def test_known_case_of_2520(self):
        """
        2520 is the smallest number that can be perfectly
        divided by each of the natural numbers 1..10
        """
        self.assertEqual(natural_num_division_streak(10), 2520)
