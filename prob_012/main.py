#!/usr/bin/env python

import time
import math

def chrono(fct):
  def ch(*v, **vv):
    t1 = time.time()
    ret = fct(*v, **vv)
    t2 = time.time()
    print("=> {} sec".format(t2-t1))
    return ret
  return ch

def triangle_number(n):
  return n * (n + 1) // 2


def decomp1(n):
  t = []
  for x in range(1, n+1):
    if n % x == 0:
      t.append(x)
  return t

@chrono
def fct1(n):
  i = 0
  while True:
    i += 1
    m = triangle_number(i)
    t = decomp1(m)
    if len(t) > n:
      return m


def decomp2(m):
  val = m
  t = [m, 1]
  tt = { m: 1, 1: 1 }
  tt = {}
  x = 1

  # Generate divisors
  while True:
    x += 1
    div = 0
    while val % x == 0:
      val = val // x
      div += 1
    if div != 0:
      tt[x] = div
    for i in range(1, div+1):
      t.append(x ** i)
    if val == 1:
      break

  t = [1]
  for k in tt:
    for i in range(0, tt[k]):
      t.append(k)

  return sorted(list(set(multi(t))))

@chrono
def fct2(n):
  i = 0
  cache = {}
  while True:
    i += 1
    m = triangle_number(i)
    t = decomp2(m)
    if len(t) >= n:
      return m


def multi(t):
  return _multi(t[0], t[1:])

def _multi(v, t):
  ret = [v]
  if len(t) == 0:
    return ret
  for i in range(len(t)):
    ret.extend(_multi(v * t[i], t[i+1:]))
  return ret


#print(fct1(200))
print(fct2(200))
