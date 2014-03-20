# What is the total of all the name scores in the file?

# file located at resources/22.txt


import re
import string

alphabet = string.uppercase

f = open('resources/22.txt', 'r')
s = f.read()
f.close()

s = re.sub('"', '', s)
s = s.split(',')
s.sort()

total = 0
for i in range(len(s)):
  name = s[i]
  score = 0
  for letter in name:
    score += alphabet.index(letter) + 1
  total += score*(i+1)

print total


