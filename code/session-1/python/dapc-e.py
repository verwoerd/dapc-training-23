n, chars = int(input()), set()
for _ in range(n):
  cc = [list(map(int, input().split())) for _ in range(int(input()))]
  min_x, min_y = (min(xs) for xs in zip(*cc))
  chars.add(tuple(sorted([(x - min_x, y - min_y) for x, y in cc])))
print(len(chars))