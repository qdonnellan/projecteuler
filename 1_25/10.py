# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import numpy as np

n = 2000000
primes = np.arange(2,n)
i = 2
while i*i < n:
    r = np.mod(primes, i) > 0
    primes = r*primes + primes*(primes == i)
    primes = primes[primes != 0]
    i += 1

print sum(primes)