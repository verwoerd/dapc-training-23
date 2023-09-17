n, recipes = int(input()), []

for _ in range(n):
  (recipe, s), end = input().split(), {}
  steps = [(sn, int(t), ds) for sn, t, d, *ds in (input().split() for _ in range(int(s)))]
  for step, t, ds in steps:
    end[step] = t + max((end[d] for d in ds), default=0)
  recipes.append((sum(t for _, t, _ in steps) / max(end.values()), recipe))

print("\n".join(name for _, name in sorted(recipes)))
