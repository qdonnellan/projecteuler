from problems_01_25.problem_03 import largest_prime_factor
from problems_01_25.plots.useful import array_from_function
import matplotlib.pyplot as plt
import numpy as np

# plot the largest prime factor for each integer
# less than the limit
LIMIT = 10000

x = np.arange(0,LIMIT)
y = array_from_function(x, largest_prime_factor)

plt.xlabel('Integer')
plt.ylabel('Largest Prime Divisor')
plt.title(
    """
    Largest Prime Divisor of Integers Less Than %s
    """% LIMIT)
    
plt.plot(x,y, ',')
plt.show()