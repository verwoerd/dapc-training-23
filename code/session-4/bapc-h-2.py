def find_numbering(st):
  new_seen = set(seen)
  ans = []
  for u, v in zip(st, [*st[1:], st[0]]):
    h, i = edges[u][v]
    ans.append((i, u))
    todo = [(v, h)]
    while todo:
      curr, h2 = todo.pop()
      new_seen.add(curr), (ns := [(neigh, t) for neigh, t in edges[curr].items() if neigh not in new_seen])
      if any(c > 1 for c in C([*((h3 for _, (h3, _) in ns)), *([h] if curr == v else [])]).values()): return False
      for neigh, (h3, i3) in ns: ans.append((i3, neigh)), todo.append((neigh, h3))
  return " ".join(str(u) for i, u in sorted(ans))


print(find_numbering(cycle) or find_numbering(cycle[::-1]) or "impossible")
