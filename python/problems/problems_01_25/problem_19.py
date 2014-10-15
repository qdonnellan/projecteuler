# How many Sundays fell on the first of the month during 
# the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# for this problem, d = 1 is Sunday, 2 is monday, etc.

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
y = 1901
d = 2 # Jan 1, 1901 was a Monday
i = 0
hit = 0
while y < 2001:
  m = months[i]

  # check for leap years
  if m == 28 and y % 4 == 0:
    if y % 100 != 0 or y % 400 == 0:
      m = 29


  # figure out day of week, if it is "1" then that's a Sunday and a hit
  d += (m-1) % 7
  if d % 7 == 1:
    hit += 1

  if i < 11: 
    i += 1
  else: # reset month index when december hits
    i = 0
    y += 1

print hit
