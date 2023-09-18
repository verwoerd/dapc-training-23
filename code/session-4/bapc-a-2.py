if K >= 3:
  i = 0
  j = len(pairs) - 1
  while True:
    s1 = xs[i]
    (s2, [k, l]) = pairs[j]
    if k != i and l != i:
      best = min(best, abs((S - s1 - s2) / (n - 3) - X))
    if i == len(xs) - 1 and j == 0:
      break
    if j == 0 or (i < len(xs) - 1 and S - s1 - s2 > X * (n - 3)):
      i = i + 1
    else:
      j = j - 1
