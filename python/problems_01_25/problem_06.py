def sum_squared_less_squared_sum(first_n):
    """
    return the result: A - B
    where A is the square of the sum of all first_n ints
    and B is the sum of the suquare of all first_n ints
    """
    A = sum(range(1,first_n+1))**2
    B = sum([x**2 for x in range(1, first_n+1)])
    return A-B
