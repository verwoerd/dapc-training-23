n = int(input())
points = [(int(c),i+1) for i,c in enumerate(input().split())]

x, y = 1,1
result = []

sqrtn = round(n**.5)
for i in range(sqrtn):
  row = points[(i*n)//sqrtn:((i+1)*n)//sqrtn]
  row.sort(reverse = i % 2)
  for j,i in row:
    result.append("%i %i" % (i,j))
    x,y = i,j

print(*result, sep='\n')
