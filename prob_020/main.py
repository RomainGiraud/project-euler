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

fact = 1
for i in range(100, 1, -1):
  fact *= i
total = 0
for i in str(fact):
  total += int(i)
print(total)
