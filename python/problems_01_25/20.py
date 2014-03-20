
#Find the sum of the digits in the number 100!

import math

n = 100
f = math.factorial(n)
s = [int(x) for x in str(f)]
print sum(s)