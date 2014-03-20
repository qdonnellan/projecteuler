# Evaluate the sum of all the amicable numbers under 10000.

def factorsum(n, s=0):
  for i in range(1,n):
    if n % i == 0:
      s += i
  return s

amicables = []
for i in range(1,10000):
  d = factorsum(i)
  a = factorsum(d)
  if i == a and i != d:
    amicables.append(i)

print amicables
print sum(amicables)


