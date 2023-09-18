def calc(cnts):
  if tuple(cnts) in ans:
    return ans[tuple(cnts)]
  best = (100, -1)
  for m in range(1, k):
    if cnts[m] > 0:
      best = min(best, (cnts[m], m))
  m = best[1]
  new_cnts = cnts[:]
  new_cnts[m] -= 1
  best = 0
  for i in range(1, k):
    if new_cnts[i] > 0:
      new_cnts[i] -= 1
      v = 0
      if m + i != k:
        new_cnts[(m + i) % k] += 1
      else:
        v += 1
      v += calc(new_cnts)
      if m + i != k:
        new_cnts[(m + i) % k] -= 1
      best = max(best, v)
      new_cnts[i] += 1
  ans[tuple(cnts)] = best
  return best
