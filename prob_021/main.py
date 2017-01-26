#!/usr/bin/env python


'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

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

def d(n):
  tab = [1]
  for i in range(2, int(n / 2) + 1):
    if n % i == 0:
      tab.append(i)
  sum = 0
  for i in tab:
    sum += i
  return sum

sum = 0
tab = []
for i in range(1, 10001):
  d1 = d(i)
  if i != d1 and i == d(d1) and not i in tab:
    print("=> {0} / {1}".format(i, d1))
    sum += i + d1
    tab.append(i)
    tab.append(d1)

print(sum)
