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

def _fibo_rec(i):
  if i == 0:
    return 0
  elif i == 1:
    return 1
  return _fibo_rec(i-1) + _fibo_rec(i-2)

@chrono
def fibo_rec(i):
  return _fibo_rec(i)

@chrono
def fibo(i):
  prev2 = 0
  prev1 = 1
  if i == 0:
    return prev2
  elif i == 1:
    return prev1

  for i in range(2, i+2):
    tmp = prev1
    prev1 = prev2 + prev1
    prev2 = tmp
  return prev2

def fibo_even(m):
  prev2 = 0
  prev1 = 1

  val = 0
  while True:
    tmp = prev1
    prev1 = prev2 + prev1
    prev2 = tmp
    if prev2 > m:
      break
    if prev2 % 2 == 0:
      val += prev2
  return val

print(fibo_even(4000000))
