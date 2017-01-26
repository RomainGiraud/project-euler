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
  for i in range(2, m+1):
    is_prime = True
    for p in primes:
      if i % p == 0:
        is_prime = False
        break
    if is_prime:
      primes.append(i)
  return primes

def check(n, m):
  for i in range(2, m + 1):
    if n % i:
      print("error: {} % {} = {}".format(n, i, n % i))
      return False
  return True


def fct1(n):
  l = list(range(1, n + 1))
  lp = prime_numbers(n)
  for i in lp:
    j = i*i
    rem = False
    while j in l:
      l.remove(j)
      j = i*i
      rem = True
    if rem:
      l.append(j)
  print(l)

def fct2(n):
  lp = prime_numbers(n)
  total = 1
  for p in lp:
    i = 2
    while True:
      t = p**i
      if t > n:
        print("test: {}".format(p ** (i - 1)))
        total *= p ** (i - 1)
        break
      i += 1
  return total


n = 20
v = fct2(n)
print("{} => {}".format(v, check(v, n)))
