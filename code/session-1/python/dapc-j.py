from math import *

n, e = (int(i) for i in input().split())
res = 0
for r in (int(i) for i in input().split()):
  res += int(pi/asin(e/2/(r+10**-10))) if 2*r >= e else 1
print(res)
