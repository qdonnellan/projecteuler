def sum_three_five(limit):
    """
    find all integers less than the limit that are
    multiples of 3 or 5 and return their sum
    """
    the_sum = 0
    for i in range(1,limit):
        if (i % 3 == 0) or (i % 5 == 0):
            the_sum += i
    return the_sum
