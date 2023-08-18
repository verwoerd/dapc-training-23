import math
n = int(input())
ps = [list(map(int, input().split())) for _ in range(n)]

def solve(ps):
  start = ps[0]
  best = ps[1]
  for p in ps[1:]:
    if p[1] / abs(p[0] - start[0]) >= best[1] / abs(best[0] - start[0]):
      best = p
  return math.atan2(best[1], abs(best[0] - start[0])) * 360 / (2 * math.pi)

ans_left = solve(ps)
ans_right = solve(ps[::-1])
print(f"{max(ans_left, ans_right):0.7f}")
