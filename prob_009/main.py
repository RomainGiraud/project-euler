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


def fct1():
  for a in range(0, 1000**4):
    finish = False
    for b in range(a+1, 1000**4):
      c1 = (1000 - a - b) ** 2
      c2 = a**2 + b**2
      s = a + b + c1
      if s > 1000:
        break
      if c1 == c2 and b < c1:
        print("{} + {} + {} = {}, abc = {}".format(a, b, c1, s, a*b*c1))
        finish = True
        break
    if finish:
      break

def fct2():
  for a in range(0, 1000**4):
    finish = False
    for b in range(a+1, 1000**4):
      c = math.sqrt(a**2 + b**2)
      s = a + b + c
      if s > 1000:
        break
      if s == 1000 and a < b and b < c:
        print("{} + {} + {} = {}, abc = {}".format(a, b, c, s, a*b*c))
        finish = True
        break
    if finish:
      break

fct2()
