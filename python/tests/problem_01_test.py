from problems.problems_01_25.problem_01 import Problem01
import unittest

class Problem01Test(unittest.TestCase):

    def test_numbers_less_than_equal_to_ten(self):
        problem = Problem01()
        problem.limit = 10
        problem.solve_problem()
        self.assertEqual(problem.solution, 23)
