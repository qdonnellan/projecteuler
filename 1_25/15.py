# Starting in the top left corner of a 2x2 grid, 
# and only being able to move to the right and down, 
# there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20x20 grid?

n, c = 40, 1
row = [c]
for k in range(1,n+1):
  c = c*(n+1-k)/k
  row.append(c)

print max(row)

# I used Pascal's triangle, calculating only the row needed (see the 
# wikipedia article and scroll down to calculating a row by itself)
