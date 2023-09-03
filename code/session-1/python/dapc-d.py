n, k = map(int, input().split())
algs = {tuple(zip(*(map(int, input().split()) for _ in ".."))) for _ in range(n)}
stack = [[(0, 0) for _ in range(k)]]
while stack:
  base = stack.pop()
  add = {alg for alg in algs if all(l <= b for (a, b), (l, h) in zip(base, alg))}
  stack.extend(add)
  algs = algs.difference(add)
print(n - len(algs))
