# What is the sum of the numbers on 
# the diagonals in a 1001 by 1001 spiral 
# formed in the same way?

def diagonal_sum(s):
  '''
  return the sum of diagonals for a square-spiral with side length s 
  where the spiral is formed by starting with 1 and spirally clockwise 
  adding 1 each time
  '''
  dSum = 1
  for shell in range(3,s+1,2):
    for n in range(4):
      corner = shell**2 - n*(shell-1)
      dSum += corner
  return dSum

print diagonal_sum(1001)
