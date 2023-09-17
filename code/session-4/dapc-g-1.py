import random
from math import *

def is_prime(i):
  if i < 0: return False
  if i not in primes.keys(): primes[i] = not any(i % x == 0 for x in range(2, int(floor(sqrt(i))) + 1))
  return primes[i]

def is_valid(p, guess, res):
  gud = [c for c, r in zip(guess, res) if r != "w"]
  for i, (c, r) in enumerate(zip(guess, res)):
    if r == "w" and (c == p[i] if c in gud else c in p): return False
    if r == "y" and (c == p[i] or c not in p): return False
    if r == "g" and c != p[i]: return False
  return True
