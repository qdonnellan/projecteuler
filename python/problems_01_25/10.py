# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import numpy as np

n = 2000000
p = np.arange(3,n,2)
i = 3
m = 0
while i*i < n:
    r = np.mod(p, i) > 0 # array of all remainders not 0
    p = r*p + p*(p == i) # array of all evenly divisible number not "i"
    p = p[p != 0] # remove all non primes divisible by i
    m += 1
    i = p[m] # set i to the next prime in the list of known primes

print sum(p)+2