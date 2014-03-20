from numpy import array

def array_from_function(x_array, function):
    """
    return an array of dependent values based on the
    independent values (x_array) and function passed
    """
    y = []
    for x in x_array:
        y.append(function(x))
    return array(y)
