#!/usr/bin/env python

import time

def chrono(fct):
  def ch(*v, **vv):
    t1 = time.time()
    ret = fct(*v, **vv)
    t2 = time.time()
    print("=> {} sec".format(t2-t1))
    return ret
  return ch

def prime_numbers(m):
  primes = [2]
  for i in range(2, m):
    is_prime = True
    for p in primes:
      if i % p == 0:
        is_prime = False
        break
    if is_prime:
      primes.append(i)
  return primes

def prime(nth):
  primes = [2]
  n = 3
  i = 1
  while True:
    is_prime = True
    for p in primes:
      if n % p == 0:
        is_prime = False
        break
    if is_prime:
      primes.append(n)
      i += 1
    if i == nth:
      break
    n += 1
  return n

print(prime(10001))
