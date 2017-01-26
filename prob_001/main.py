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

total = 0
for i in range(0, 1000):
  if i % 3 == 0 or i % 5 == 0:
    total += i
    #print('{}'.format(i), end=' ')

print(total)
