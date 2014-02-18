# Find the value of d for which 1/d contains the longest 
# recurring cycle in its decimal fraction part

def longest_recurring_cycle(limit):
    '''
    returns the value d less than the limit for which 1/d contains the longest recurring cylce in its
    decimal notation. For example, the fraction 1/3 has a recurring cycle of 1
    '''
    max_cycle = 1
    max_cycle_d = 3
    for n in range (limit, 3, -1):
        length = cycle_length(n)
        if length and length > max_cycle:
            max_cycle = length
            max_cycle_d = n
    return max_cycle, max_cycle_d

def assert_prime_number(n):
    '''
    return true if number is prime, false otherwise
    '''
    status = False
    s = 2
    while n % s != 0 and s*s < n and n > 1: # only check until s*s < n
        s += 1
    if s*s > n and n > 1: # if n is prime to s*s > n, it will be prime
        status = True
    return status

def cycle_length(n):
    '''
    determine the cycle length of n or False if n is not prime
    '''
    if assert_prime_number(n) and n%2 != 0 and n%5 != 0:
        count = 1
        r = 10 % n
        while r != 1:
            r = r * 10 % n
            count += 1
        return count
    else:
        return False


