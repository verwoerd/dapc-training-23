(n, q), units = map(int, input().split()), dict()

for _ in range(n):
    a, b = input()[2:].split(" = ")
    x, b = b.split()
    x = float(x)
    if a not in units: units[a] = dict()
    if b not in units: units[b] = dict()
    units[a][b], units[b][a] = x, 1 / x

for _ in range(q):
    a, b = input().split(" to ")
    x, a = a.split()
    seen, todo = {a: float(x)}, [a]
    while todo:
        curr = todo.pop()
        if curr == b:
            print(seen[b])
            break
        for k, v in units[curr].items():
            if k not in seen:
                seen[k] = seen[curr] * v
                todo.append(k)
    else:
        print("impossible")