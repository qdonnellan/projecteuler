# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 
# 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

n = 1
for a in range(100,1000):
    for b in range(100,1000):
        if str(a*b)[::-1] == str(a*b): #check if palindrome
            if a*b > n: # check if larger than current palindrome
                n = a*b
print n