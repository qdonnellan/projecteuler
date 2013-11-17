# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.

# What is the 10001st prime number?
import numpy as np

i = 1
n = 2
while i < 2:
    f = n + 1
    while f % n != 0:
        print f, n
        n += 1
    i += 1

print n
   