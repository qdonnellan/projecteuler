def natural_num_division_streak(max_N):
    """
    return the smallest number perfectly divisivbly by each
    of the natural numbers 1..max_N
    """

    n = max_N
    i = max_N
    while i > 0:
        if  n % i == 0: # see if divisible by i
            i -= 1 # if so, check the next i
        else:
            i = max_N # if not, reset the search
            n += max_N # increment by the next number*
    return n

    """
    * you should increment by the next number divisible by the
    largest factor in the search
    """
