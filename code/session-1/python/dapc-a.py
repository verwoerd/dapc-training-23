n,l = [int(i) for i in input().split()]
a = sorted([input() for i in range(n)])
t = 1
p = 0
for i in range(1,n):
  for j in range(l):
    if a[i-1][j] != a[i][j]:
      t += j+1 + max(j-p,0)
      p = j
      break
print(t)