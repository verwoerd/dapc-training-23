n, k = map(int, input().split())
w = list(map(int, input().split()))
ans = 0
cnt = [0] * k
# modulo
for x in w:
  if x % k == 0:
    ans += 1
  else:
    cnt[x % k] += 1
# pairs
for i in range(1, k // 2):
  x = min(cnt[i], cnt[k - i])
  cnt[i] -= x
  cnt[k - i] -= x
  ans += x
if k % 2 == 0:
  x = cnt[k // 2] // 2
  cnt[k // 2] -= 2 * x
  ans += x
# Left with at most 3 non-empty values, and possibly k/2.
ans = {tuple([0] * k): ans}
print(sum(w) // k - calc(cnt))
