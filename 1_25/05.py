# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all 
# of the numbers from 1 to 20?

n = 20
i = 20
while i > 10:
    # if the remainder is zero search for next lowest until less than 10
    if  n % i == 0:
        i -= 1 
    else:
    # if the remainder is not zero, restart search at 20 and increment by 20
        i = 20
        n += 20
print n

