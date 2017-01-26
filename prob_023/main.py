#!/usr/bin/env python

'''
'''

import time
import math
import sys

def chrono(fct):
  def ch(*v, **vv):
    t1 = time.time()
    ret = fct(*v, **vv)
    t2 = time.time()
    print("=> {} sec".format(t2-t1))
    return ret
  return ch

def proper_div(n):
  tab = [1]
  for i in range(2, int(n / 2) + 1):
    if n % i == 0:
      tab.append(i)
  return tab

def sum(l):
  total = 0
  for i in l:
    total += i
  return total


imax = 28123
nmax = int(imax / 2)

non_abundant = []
for i in range(1, imax + 1):
  if i >= sum(proper_div(i)):
    non_abundant.append(i)

for i in range(1, imax + 1):




total = 0

for i in range(28120, 28123 + 1 + 1):
  if i % 2 != 0:
    continue
  n = int(i / 2)
  b = False
  print(n)
  if n < sum(proper_div(n)):
    total += i
    b = True
  print("{0} => {1}".format(i, b))

#print(total)
print(sum(proper_div(28124)))
