def even_fibsum(limit):
    """
    return the sum of all even terms in the Fibonacci
    series where the largest term is less than the limit
    """
    nums = [1,2]
    the_sum = 0
    while nums[-1] < limit:
        if nums[-1] % 2 == 0:
            the_sum += nums[-1]
        nums.append(nums[-1]+nums[-2])

    return the_sum
