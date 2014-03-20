from problems_01_25.problem_02 import even_fibsum
import matplotlib.pyplot as plt
import numpy as np

# plot the sum of even integers in a 
# Fibbonicci series where the largest
# term is less than the limit below
LIMIT = 100000

x = np.arange(0,LIMIT)
y = []
for xi in x:
    y.append(even_fibsum(xi))
    
y = np.array(y)

plt.xlabel('Largest term in Fib. Series')
plt.ylabel('Sum of terms')
plt.plot(x,y, '-')

# this graph looks great in a log-log scale!
plt.xscale('log')
plt.yscale('log')
plt.show()
