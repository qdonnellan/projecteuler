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
            if str(a*b)[::-1] == str(a*b): #is palindrome?
                if a*b > n: #is this larger that the current?
                    n = a*b #we have a new winner!

    return n
