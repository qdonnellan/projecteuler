# By starting at the top of the triangle below and 
# moving to adjacent numbers on the row below, the 
# maximum total from top to bottom is 23.


#3
#7 4
#2 4 6
#8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:
t= '''
              75
             95 64
            17 47 82
           18 35 87 10
          20 04 82 47 65
         19 01 23 75 03 34
        88 02 77 73 07 63 67
       99 65 04 28 06 16 70 92
      41 41 26 56 83 40 80 70 33
     41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
   70 11 33 28 77 73 17 78 39 68 17 57
  91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''
# reading the triangle into a list
t = t.split('\n')
t = [x.strip(' ') for x in t if x != '']
tn = []
for row in t:
  tn.append([int(x) for x in row.split(' ')])
# end read

# the method is simple: for each second to last row, 
# take the two options for each number in the row and pick the max
# then replace the second to last row with the sum
# do this until there are no more rows left!
while len(tn) > 1:
  for i in range(len(tn[-2])):
    tn[-2][i] =  max([tn[-1][i], tn[-1][i+1]]) + tn[-2][i]
  del tn[-1]

print tn
