import unittest
from problem_29 import distinct_powers

class Problem29Test(unittest.TestCase):
  '''
  test class for the implementation of 
  problem Euler problem 29
  '''

  def test_spiral_with_side_length_5(self):
    '''
    test that for 2 <= a <= 5 and 2 <= b <= 5, 
    there are 15 unique combinations of a^b
    '''
    n = distinct_powers(a_limit = 5, b_limit = 5)
    self.assertEqual(n, 15)
