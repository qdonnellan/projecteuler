from problems.problems_01_25.problem_02 import Problem02
import unittest

class Problem02Test(unittest.TestCase):
    """
    test the implementation of Project Euler Problem #2
    """

    def test_terms_less_than_20(self):
        """
        test problem 2 case were limit is 20

        there are 2 terms (2,8) less than 20
        in the Fibbonacci series that are even, their
        sum is 10
        """
        problem = Problem02()
        problem.limit = 20
        problem.solve_problem()
        self.assertEqual(problem.solution, 10)
