from math import sqrt

n = int(input())
ps = []
for _ in range(n):
  ps.append(list(map(int, input().split())))
ps.sort()
W = 100
ans = 3 * 10**9
for (i, (x1, y1, z1)) in enumerate(ps):
  for j in range(max(0, i - W), i):
    (x2, y2, z2) = ps[j]
    d = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
    ans = min(ans, d)
print(ans)
