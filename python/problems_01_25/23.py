
def d(n):
  s = 1
  t = n**0.5
  for i in range(2, int(t)+1):
      if n % i == 0:
          s += i + n / i
  if t == int(t):
      s -= t # don't count square root and itself (would be a double factor)
  return s

limit = 20162
s = 0
abn = set()
for n in range(1, limit):
    if d(n) > n:
        abn.add(n)
    if not any( (n-a in abn) for a in abn ):
        s += n
print s

# I've basically taken this solutin from forums, want to come back to it later and optimize