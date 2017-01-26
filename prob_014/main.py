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

def syr(n):
  if n == 1:
    return [1]
  if n % 2 == 0:
    t = [n]
    t.extend(syr(n // 2))
    return t
  t = [n]
  t.extend(syr(3 * n + 1))
  return t

def syr2(n):
  if n == 1:
    return [1]
  if n % 2 == 0:
    t = [n]
    t.extend(syr2(n // 2))
    return t
  t = [n]
  t.extend(syr2((3 * n + 1) // 2))
  return t

def syr_optim(n):
  if n <= 1:
    return 1
  if n % 2 == 0:
    return 1 + syr_optim(n // 2)
  return 1 + syr_optim(3 * n + 1)

def syrb_optim(n):
  i = 1
  while True:
    if n == 1:
      break
    if n % 2 == 0:
      n //= 2
    else:
      n = 3 * n + 1
    i += 1
  return i

@chrono
def fct1(n):
  m = 0
  j = 0
  for i in range(1, n+1):
    v = syr_optim(i)
    if v > m:
      m = v
      j = i
  return (m, j)

@chrono
def fct2(n):
  m = 0
  j = 0
  for i in range(1, n+1):
    v = syrb_optim(i)
    if v > m:
      m = v
      j = i
  return (m, j)

#print(fct1(1000))
print(fct2(1000000))
