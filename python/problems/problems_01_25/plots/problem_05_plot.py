from problems_01_25.problem_05 import natural_num_division_streak
from problems_01_25.plots.useful import array_from_function
import matplotlib.pyplot as plt
import numpy as np

#trying numbers over 18 takes a long time!
x = np.arange(1,15)
y = array_from_function(x, natural_num_division_streak)

plt.plot(x, y, '-')

#plot follows a linear pattern when y is log-scaled
plt.yscale('log')


plt.xlabel('Streak of N-natural numbers required')
plt.ylabel('Smallert number that is perfectly divisible')
plt.show()


