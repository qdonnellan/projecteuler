from problems.problems_01_25.problem_01 import Problem01
import unittest

class Problem01Test(unittest.TestCase):

    def test_numbers_less_than_equal_to_ten(self):
        problem = Problem01()
        problem.limit = 10
        problem.find_multiples_of_3_or_5_less_than_limit()
        self.assertEqual(problem.sum_multiples(), 23)
