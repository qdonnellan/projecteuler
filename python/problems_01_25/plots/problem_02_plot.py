from problems_01_25.problem_02 import even_fibsum
from problems_01_25.plots.useful import array_from_function
import matplotlib.pyplot as plt
import numpy as np

# plot the sum of even integers in a 
# Fibbonicci series where the largest
# term is less than the limit below
LIMIT = 10000

x = np.arange(0,LIMIT)
y = array_from_function(x, even_fibsum)

plt.xlabel('Largest term in Fib. Series')
plt.ylabel('Sum of terms')
plt.title(
    """
    Sum of even terms in a Fibonacci series
    """
)
plt.plot(x,y, '-')

# this graph looks great in a log-log scale!
plt.xscale('log')
plt.yscale('log')
plt.show()
