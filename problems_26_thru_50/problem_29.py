# How many distinct terms are in the sequence 
# generated by ab for 2 <= a <= 100 and 2 <= b <= 100?

def distinct_powers(a_limit, b_limit):
  '''
  returns the number of distinct terms in the sequence 
  generated by producing all combinations of a^b such that
  2 <= a <= a_limit and 2 <= b <= b_limit
  '''
  s = set()
  for a in range(2, a_limit+1):
    for b in range(2, b_limit+1):
      s.add(a**b)
  return len(s)