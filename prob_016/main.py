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

@chrono
def f(n):
  t = 0
  for i in str(2**n):
    t += int(i)
  print(t)

@chrono
def f2(n):
  t = 0
  for i in str(2 << (n - 1)):
    t += int(i)
  print(t)

f(15)
f(1000)
f2(1000)
