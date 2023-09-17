import random

w, h = map(int, input().split())
xs, highest_x, highest_y = list(range(1, w + 1)), 1, 1
random.shuffle(xs)
for x in xs:
  print(f"? {x} {min(highest_y, h)}")
  if input() == "building":
    low, high = highest_y + 1, h + 1
    while low < high:
      mid = (low + high) // 2
      print(f"? {x} {mid}")
      if input() == "building": low = mid + 1
      else: high = mid
    highest_x, highest_y = x, high
print(f"! {highest_x} {highest_y - 1}")
