# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from itertools import permutations

s = permutations('0123456789')
s = list(s)
print s[999999] #index 999999 is the 1,000,000th element