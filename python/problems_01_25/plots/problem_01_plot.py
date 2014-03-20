from problems_01_25.problem_01 import sum_three_five
import matplotlib.pyplot as plt
import numpy as np

# plot the sum of integers less than LIMIT
# which are multiples of 3 or 5
LIMIT = 100

x = np.arange(0,100,1)
y = []
for xi in x:
    y.append(sum_three_five(xi))
    
y = np.array(y)

plt.xlabel('Limit')
plt.ylabel('Sum of terms')
plt.plot(x,y, '-')
plt.show()
