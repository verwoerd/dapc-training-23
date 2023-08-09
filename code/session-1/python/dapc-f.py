import sys

x, y = [int(x) / 100 for x in sys.stdin.readline().split()]
print((x * (1 - y)) / (y * (1 - x)))
