ans, i = 0, 0
for j in range(1, int(input()) + 1):
  print("?", i, j)
  if input() == "absent":
    ans += 1
    i = j
print("!", ans)
