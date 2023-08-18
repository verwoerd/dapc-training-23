def calculate(wind):
  end = wind[-2:]
  if wind[-2:] not in "NESWN": end = end[::-1]
  low = "NESWN".index(end) * 90
  high = low + 90
  curr = low + 45
  for c in wind[-3::-1]:
    if end.index(c) == 0:
      high = curr
    else:
      low = curr
    curr = (low + high) / 2
  return curr

X, Y = sorted("NESW".index(d[0]) * 90 if len(d) == 1 else calculate(d) for d in input().split())
print(min(Y - X, 360 + X - Y))
