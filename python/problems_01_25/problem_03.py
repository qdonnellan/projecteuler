def largest_prime_factor(number):
    """
    return the largest prime factor of the number
    """
    i = 2
    while i * i < number:
        while number % i == 0:
            number = number / i
        i += 1
    return number
