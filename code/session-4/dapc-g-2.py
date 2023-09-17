def perform_guess(guess_int):
  global left
  _, res = print(guess := str(guess_int)), input().strip()
  if res == "ggggg": return True
  left = [p for p in left if p != guess and is_valid(p, guess, res)]

n, primes = int(input()), {0: False, 1: False, 2: True, 3: True}
primes_list = [str(i) for i in range(100_000) if is_prime(i) and i > 10_000]
start_a, start_b = next((a, b) for a in primes_list for b in primes_list if sorted(f"{a}{b}") == list("0123456789"))

for _ in range(n):
  left = list(primes_list)
  if perform_guess(start_a) or perform_guess(start_b): continue
  while not perform_guess(random.choice(left)): pass
