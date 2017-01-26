#!/usr/bin/env python

import time

def chrono(fct):
  def ch(*v, **vv):
    t1 = time.time()
    ret = fct(*v, **vv)
    t2 = time.time()
    print("time: {} sec".format(t2-t1))
    return ret
  return ch


@chrono
def prime_factor_1a(n):
  tab=[n]
  while True:
    ntab=[]
    for t in tab:
      not_del = True
      for i in range(2, t):
        if t % i == 0:
          m = t // i
          ntab.append(m)
          not_del = False
      if not_del:
        ntab.append(t)
    ntab=set(ntab)
    if set(tab) == ntab:
      break
    tab=list(ntab)
  return ntab


@chrono
def prime_factor_1b(n):
  tab=[n]
  while True:
    ntab=[]
    for t in tab:
      not_del = True
      for i in range(2, t):
        m = t // i
        if m < i:
          break
        if t % i == 0:
          ntab.append(i)
          ntab.append(m)
          not_del = False
      if not_del:
        ntab.append(t)
    ntab=set(ntab)
    if set(tab) == ntab:
      break
    tab=list(ntab)
  return ntab


@chrono
def prime_factor_3a(n):
  tab = [n]
  cache = {}
  while True:
    ntab = []
    for t in tab:
      if t in cache:
        continue
      cache[t] = []
      not_del = True
      for i in range(2, t):
        if t % i == 0:
          m = t // i
          ntab.append(m)
          cache[t].append(m)
          not_del = False
      if not_del:
        ntab.append(t)
    ntab = set(ntab)
    if set(tab) == ntab:
      break
    tab = list(ntab)

  tmp = []
  for t in cache:
    if len(cache[t]) == 0:
      tmp.append(t)
  return tmp


@chrono
def prime_factor_3b(n):
  tab = [n]
  cache = {}
  quit = False
  while quit:
    ntab = []
    for t in tab:
      if t in cache:
        continue
      cache[t] = []
      not_del = True
      for i in range(2, t):
        m = t // i
        if m < i:
          quit = True
          break
        if t % i == 0:
          ntab.append(i)
          ntab.append(m)
          cache[t].append(i)
          cache[t].append(m)
          not_del = False
      if not_del:
        ntab.append(t)
      if quit:
        break
    ntab = set(ntab)
    if set(tab) == ntab:
      break
    tab = list(ntab)

  tmp = []
  for t in cache:
    if len(cache[t]) == 0:
      tmp.append(t)
  return tmp


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

@chrono
def prime_factor_2(n):
  primes = prime_numbers(n // 2)
  tab = []
  for i in primes:
    if n % i == 0:
      tab.append(i)
  return tab


@chrono
def prime_factor_4a(n):
  tab = []
  for i in range(1, (n+1)):
    if n % i == 0:
      tab.append(i)
      tab.append(n // i)
  tab.sort()
  stab = list(set(tab))
  stab.sort()
  print("size: {} => {}".format(len(tab), tab))
  print("size: {} => {}".format(len(stab), stab))

@chrono
def prime_factor_4b(n):
  tab = []
  for i in range(1, (n+1) // 2):
    if n % i == 0:
      tab.append(i)
      tab.append(n // i)
  tab.sort()
  stab = list(set(tab))
  stab.sort()
  print("size: {} => {}".format(len(tab), tab))
  print("size: {} => {}".format(len(stab), stab))

@chrono
def prime_factor_4c(n):
  tab = []
  for i in range(1, n+1):
    m = n // i
    if m < i:
      break
    if n % i == 0:
      tab.append(i)
      tab.append(m)
  tab.sort()
  stab = list(set(tab))
  stab.sort()
  print("size: {} => {}".format(len(tab), tab))
  print("size: {} => {}".format(len(stab), stab))


@chrono
def prime_factor_5a(n):
  factor = 2
  lastFactor = 1
  while n > 1:
    if n % factor == 0:
      lastFactor = factor
      m = n // factor
      print("{} / {} = {}".format(n, factor, m))
      n = m
      while n % factor == 0:
        m = n // factor
        print(" |- {} / {} = {}".format(n, factor, m))
        n = m
    factor = factor + 1
  print(lastFactor)



# 13195 are 5, 7, 13 and 29
#n = 13195
#n = 13195424
n = 600851475143
print("=> {}".format(n))
#print(prime_factor(n))
print(prime_factor_1b(n))
print(prime_factor_5a(n))
