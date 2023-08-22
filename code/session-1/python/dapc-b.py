n,k = [int(i) for i in input().split()]
a = sorted([(int(c),i) for i,c in enumerate(input().split())])
best = 0
for j,(c,i) in enumerate(a):
    best = max(best, i-j)
print(((best-1) // (k-1)) + 1)