# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

#n = 600851475143

def isprime(x):
    known_primes = [2,3,5,7,9,11,13,17,19,23,29]
    if x in known_primes:
        return True
    elif (x % 2 == 0):
        return False
    else:
        limit = int(x**0.5) + 1
        check = 2
        while check <= limit:
            if (x % check == 0) and (x != check):
                return False
                break
            else:
                check += 1
        
        

n = 13195000
check  = n
while check > 0:
    if n % check == 0:
        if isprime(check):
            print check
            break
    check -= 1

