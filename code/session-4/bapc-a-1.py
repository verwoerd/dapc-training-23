from bisect import bisect

n, K, X = map(int, input().split())

xs = sorted(list(map(int, input().split())))
S = sum(xs)

pairs = []
for i in range(n):
  for j in range(i):
    pairs.append((xs[i] + xs[j], [i, j]))
pairs.sort()

# k = 0
best = abs(S / n - X)
if K >= 1:
  for s in xs:
    best = min(best, abs((S - s) / (n - 1) - X))
if K >= 2:
  for (s, ij) in pairs:
    best = min(best, abs((S - s) / (n - 2) - X))

