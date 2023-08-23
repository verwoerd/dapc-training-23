from collections import deque

h, w = map(int, input().split())
plots = [list(map(int, input().split())) for _ in range(h)]
neighs = [[[min((abs(neigh - dest), abs(neigh - plots[y][x]), xx, yy) for xx, yy, neigh in
                ((xx, yy, plots[yy][xx]) for xx, yy in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))
                 if 0 <= xx < w and 0 <= yy < h))[2:]
            for x in range(w)] for y in range(h)] for dest in range(1, w * h + 1)]


def find_paths(dest_x, dest_y, dest):
  seen, queue = [[0] * w for _ in range(h)], deque([(dest_x, dest_y, 0)])
  while queue:
    x, y, dist = queue.popleft()
    for xx, yy in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
      if 0 <= xx < w and 0 <= yy < h and neighs[dest - 1][yy][xx] == (x, y) and not seen[yy][xx]:
        queue.append((xx, yy, dist + 1))
        seen[yy][xx] = dist + 1
  return seen


paths = [[find_paths(x, y, plots[y][x]) for x in range(w)] for y in range(h)]
best = min((max(paths[dest_y][dest_x][kiosk_y][kiosk_x] or 1e9 for dest_y in range(h) for dest_x in range(w)),
            plots[kiosk_y][kiosk_x]) for kiosk_y in range(h) for kiosk_x in range(w))
print("impossible") if best[0] == 1e9 else print(*best[::-1])