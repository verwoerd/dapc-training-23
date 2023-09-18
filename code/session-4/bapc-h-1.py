from collections import defaultdict, Counter as C

n, edges, stack, seen, todo = int(input()), defaultdict(dict), [], set(), [[1]]
for i in range(n):
  u, v, h = map(int, input().split())
  edges[u][v] = (h, i)
  edges[v][u] = (h, i)

if any(any(c > 2 for c in C(h for h, _ in edges[u].values()).values()) for u in edges): print("impossible"), exit()

while True:
  if (curr := todo[-1].pop()) in seen: break
  stack.append(curr), seen.add(curr)
  todo.append([x for x in edges[curr].keys() if len(stack) == 1 or stack[-2] != x])
  while todo and not todo[-1]:
    if not stack: print("impossible"), exit()
    todo.pop(), seen.remove(stack.pop())

cycle = [curr]
while stack:
  u = stack.pop()
  if u == curr: break
  cycle.append(u)
while stack: seen.remove(stack.pop())
