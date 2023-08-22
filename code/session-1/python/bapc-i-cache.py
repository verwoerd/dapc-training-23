(n, q), units, conversions = map(int, input().split()), dict(), dict()

for _ in range(n):
    _, a, _, x, b = (t(s) for t, s in zip((str, str, str, float, str), input().split()))
    units = {a: dict(), b: dict(), **units}
    units[a][b], units[b][a] = x, 1 / x

for a in units:
    seen, todo = {a: 1.0}, [a]
    while todo:
        curr = todo.pop()
        for k, v in units[curr].items():
            if k not in seen: seen[k], _ = seen[curr] * v, todo.append(k)
    conversions[a] = seen

for x, a, _, b in ((t(s) for t, s in zip((float, str, str, str), input().split())) for _ in range(q)):
    print(float(x) * conversions[a][b] if a in conversions and b in conversions[a] else "impossible")