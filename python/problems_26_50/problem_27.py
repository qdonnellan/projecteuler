# Find the product of the coefficients, a and b, for the quadratic 
# expression n^2 + an + b that produces the maximum number of primes for 
# consecutive values of n, starting with n = 0.

from problem_26 import assert_prime_number

def quadratic_prime(a,b,n):
  '''
  return the value of n^2 + an + b if prime and False otherwise
  '''
  c = n**2 + a*n + b
  if assert_prime_number(c):
    return c
  else:
    return False

def longest_quad_prime_streak(low_limit, high_limit):
  '''
  for a range of numbers [low_limit:high_limit] find the coefficients a and 
  that produce the longest consecutive streak of quadratic primes using
  n^2 + an + b
  '''
  streak = 0
  saved_a, saved_b = 0, 0
  for a in range(low_limit, high_limit+1):
    for b in range(low_limit, high_limit+1):
      n = 0
      while quadratic_prime(a,b,n):
        n += 1
      if n > streak:
        streak = n
        saved_a, saved_b = a, b
  return saved_a, saved_b, streak



