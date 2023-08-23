a, b, c = map(int, input().split())
w = input()
s = input()
for x in w:
  off = 0
  on = 10**9
  for y in s:
    if x == y:
      on = min(on, off + c) + b
      off = on + c
    else:
      on = on + a
  print(off)