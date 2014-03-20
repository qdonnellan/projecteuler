def digit_powers_sum(nth_degree):
  '''
  return the sum of the numbers which are equal to the sum
  of the nth_degree of their digits. 1634 is one such number
  for nth_degree = 4:

  1643 = 1^4 + 6^4 + 3^4 + 4^4
  '''
  total_sum = 0
  upper_limit = 354294 # need to make this dynamic 
  for i in range(10,upper_limit+1):
    stringi = str(i)
    sumi = 0
    for digit in stringi:
      sumi += int(digit)**nth_degree

    if sumi == i:
      total_sum += sumi

  return total_sum
