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

def is_palin(n):
  n = str(n)
  l = len(n)
  ret = True
  for i in range(0, l // 2):
    if n[i] != n[l-1-i]:
      ret = False
      break
  return ret


@chrono
def fct1(size=3):
  v = 0
  n = (10 ** size) - 1
  m = (10 ** (size - 1)) - 1
  for i in range(m, n+1):
    for j in range(m, n+1):
      k = i * j
      if is_palin(k):
        if k > v:
          v = k
  return v


@chrono
def fct2(size=3):
  v = 0
  n = (10 ** size) - 1
  m = (10 ** (size - 1)) - 1
  for i in range(n, m, -1):
    for j in range(i, m, -1):
      k = i * j
      if is_palin(k) and k > v:
        v = k
  return v


@chrono
def fct3(size=3):
  v = 0
  n = (10 ** size) - 1
  m = (10 ** (size - 1)) - 1
  for i in range(n, m, -1):
    for j in range(i, m, -1):
      k = i * j
      if k < v:
        break
      if is_palin(k):
        v = k
  return v

print(fct1())
print(fct2())
print(fct3())
