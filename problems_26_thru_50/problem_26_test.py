import unittest
from problem_26 import longest_recurring_cycle, cycle_length, assert_prime_number

class Problem26Test(unittest.TestCase):
  '''
  test the implementation of problem 26
  '''

  def test_cycle_length(self):
    '''
    test that the cycle length program works as expected
    '''
    self.assertEqual(cycle_length(2), False)
    self.assertEqual(cycle_length(7), 6)
    self.assertEqual(cycle_length(6), False)

  def test_assert_prime_number(self):
    '''
    test the implementation of my prime number assertion function
    '''
    self.assertEqual(assert_prime_number(0), False)
    self.assertEqual(assert_prime_number(1), False)
    self.assertEqual(assert_prime_number(4), False)
    self.assertEqual(assert_prime_number(7), True)
    self.assertEqual(assert_prime_number(571), True)

  def test_longest_recurring_cycle(self):
    '''
    test that the longest_recurring_cycle function works as expected for small numbers
    For example, for numbers <= 10, the longest cycle is 6 (142857)
    '''
    cycle_length, d = longest_recurring_cycle(10)
    self.assertEqual(d, 7)
    self.assertEqual(cycle_length, 6)