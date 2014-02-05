import unittest
from problem_30 import digit_powers_sum

class Problem30Test(unittest.TestCase):
  '''
  test class for the implementation of 
  problem Euler problem 30
  '''

  def test_4th_digit_powers_sum(self):
    '''
    test the known case for 4th powers sum
    '''
    self.assertEqual(digit_powers_sum(4), 19316)

