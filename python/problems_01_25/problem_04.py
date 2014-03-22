def largest_palindrome(n_digit):
    """
    return the largest palindrome which is the product
    of 2 n_digit numbers

    it is worth noting that the very useful extended slice [::-1]
    is used here to reverse the string, you should use it too!
    """
    n = 1
    lower_limit = 10**(n_digit-1)
    upper_limit = 10**(n_digit)

    for a in range(lower_limit,upper_limit):
        for b in range(lower_limit,upper_limit):
            if a*b > n: #if the product isn't larger, forget it!
                if str(a*b)[::-1] == str(a*b): #is palindrome?
                    n = a*b #we have a new winner!

    return n


    """
    Note:

    there is probably a better way to do this which is more
    efficient: Start with the product of two numbers that
    is guaranteed to be largest (for 3 digit numbers that is:
    999 x 999). Then, work your way down a chain of products
    such that the result of each subsequent product is
    guaranteed to be larger than every product yet to be
    computed. In this way, you could stop as soon as you detected
    the first palindrome instead of continuing on through
    useless products all the way down to 100x100
    """
