def nth_prime(nth):
    """
    return the nth prime number

    For Example: nth_prime(4) returns 7:
    2, 3, 5, [7]
    """
    known_primes = 0
    candidate = 1
    while known_primes < nth:
        d = 2 # d is a current divisor
        candidate += 1
        while (candidate % d != 0) and (d*d < candidate):
            d += 1
        if d*d > candidate:
            known_primes += 1 # we've found another prime!

    return candidate
