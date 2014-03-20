import unittest
from problem_28 import diagonal_sum

class Problem28Test(unittest.TestCase):
  '''
  test class for the implementation of 
  problem Euler problem 28
  '''

  def test_spiral_with_side_length_5(self):
    '''
    sum of diagonals for a 5 length spiral should be 101
    '''
    self.assertEqual(diagonal_sum(5), 101)
