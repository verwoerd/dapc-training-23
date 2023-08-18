from math import sqrt
n, x = map(int, input().split())
A = list(map(int, input().split()))
y = sum(map(lambda a: a**2, A)) / n
print(*[0 if y == 0 else sqrt(x / y) * a for a in A])
