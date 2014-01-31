import unittest
from problem_27 import quadratic_prime, longest_quad_prime_streak

class Problem27Implementation(unittest.TestCase):
  '''
  test my problem 27 implementation
  '''
  def test_quadratic_prime(self):
    '''
    quadratic_prime(1,41,0) should return 41
    quadratic_prime(0,0,2) should return False)
    '''
    self.assertEqual(quadratic_prime(1,41,0), 41)
    self.assertFalse(quadratic_prime(0,0,2))

  def test_known_coefficients(self):
    '''
    longest streak less than inside [0:41] should be 40 with the test_known_coefficient
    a = 1, b = 41 and the streak is 40 primes
    '''
    a, b, streak = longest_quad_prime_streak(0, 41)
    self.assertEqual(a,1)
    self.assertEqual(b, 41)
    self.assertEqual(streak, 40)
