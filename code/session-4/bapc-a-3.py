if K >= 4:
  for (s1, [i, j]) in pairs:
    s2 = S - s1 - (n - 4) * X
    idx = bisect(pairs, (s2, []))
    # Find first position to the left and right disjoint with ij
    for idx2 in range(idx - 1, -1, -1):
      s2, kl = pairs[idx2]
      if i not in kl and j not in kl:
        best = min(best, abs((S - s1 - s2) / (n - 4) - X))
        break
    for idx2 in range(idx, len(pairs)):
      s2, kl = pairs[idx2]
      if i not in kl and j not in kl:
        best = min(best, abs((S - s1 - s2) / (n - 4) - X))
        break

print(best)
