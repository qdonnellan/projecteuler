# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

# trying to find an alternate to using numpy

n = 2000000
i = 3
p = [2] + range(3,n,2)
m = 1
while i*i < n:
    p = [x for x in p if x==i or x % i != 0]
    m += 1
    i = p[m]
print sum(p)