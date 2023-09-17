class S:
  def __init__(self, a, b, c): self.a, self.b, self.c = a, b, c

  def getStart(self): return (self.a - self.b) // (2 * self.a)

  def getScore(self):
    x = self.getStart()
    return self.a * x * x + self.b * x + self.c

  def intersect(self, s): return self.getStart() + self.a >= s.getStart()

  def merge(self, s):
    return S(self.a + s.a, self.b + 2 * self.a * s.a + s.b, self.c + self.a * self.a * s.a + self.a * s.b + s.c)

n, A, B = int(input()), [S(1, -2 * a, a * a) for a in map(int, input().split())], []
for a in A:
  while B and B[-1].intersect(a): a = B.pop().merge(a)
  B.append(a)
print(sum(s.getScore() for s in B))
