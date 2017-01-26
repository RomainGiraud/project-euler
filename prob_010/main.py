#!/usr/bin/env python

import time

from functools import reduce
import math

def chrono(fct):
  def ch(*v, **vv):
    t1 = time.time()
    ret = fct(*v, **vv)
    t2 = time.time()
    print("=> {} sec".format(t2-t1))
    return ret
  return ch

def is_prime(n):
  for i in range(n-1, 2, -1):
    if n % i == 0:
      return False
  return True

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

def fct1(n):
  l = prime_numbers(n)
  v = reduce(lambda x, y: x + y, l)
  print("{}\n{} => {}\n------------".format(l, v, is_prime(v)))

def fct2(n):
  for i in range(0, len(l)):
    print(i)
    if l[i] != 0:
      for j in range(i + 1, len(l)):
        if l[j] == 0:
          continue
        if l[j] % l[i] == 0:
          l[j] = 0
  return [x for x in l if x != 0]

def fct3(n):
  l = list(range(2, n+1))
  i = 0
  while True:
    j = i + 1
    while True:
      if l[j] % l[i] == 0:
        del l[j]
      else:
        j += 1
      if j >= len(l):
        break
    i += 1
    if i > math.sqrt(n):
      break
  return l

def display(n):
  l = fct3(n)
  v = reduce(lambda x, y: x + y, l)
  print("{}\n{} => {}\n------------".format(l, v, is_prime(v)))

display(20)
display(200)
display(2000)

print(math.sqrt(20))
