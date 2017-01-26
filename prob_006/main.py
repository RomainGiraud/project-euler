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

def fct1(n):
  l = list(range(1, n + 1))
  t1 = 0
  t2 = 0
  for i in l:
    t1 += i ** 2
    t2 += i
  t2 **= 2
  return t2 - t1



print(fct1(10))
print(fct1(100))
