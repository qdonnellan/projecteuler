# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.

# What is the 10001st prime number?

i = 1
n = 1
while i <=  10001:
    s = 2
    n += 1
    while n % s != 0 and s*s < n: # only check until s*s < n
        s += 1
    if s*s > n: # if n is prime to s*s > n, it will be prime
        i += 1
    
print n
        
        
        
