# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import numpy as np

n = 2000000
p = np.arange(3,n,2)
i = 3
while i*i < n:
    r = np.mod(p, i) > 0 # array of all remainders not 0
    p = r*p + p*(p == i) # array of all evenly divisible number not "i"
    p = p[p != 0] # remove all non primes divisible by i
    i += 2

print sum(p)+2