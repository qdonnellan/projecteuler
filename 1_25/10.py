# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

# I'm using my solution to problem #7 to help me here

n = 5
the_sum = n
while n < 2000000:
    s = 2
    n += 2
    while n % s != 0 and s*s < n: # only check until s*s < n
        s += 1
    if s*s > n: # if n is prime to s*s > n, it will be prime
        the_sum += n
    
print the_sum