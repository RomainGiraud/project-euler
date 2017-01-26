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

def f(n):
  if n == 1:
    return 2
  return f(n - 1) + n * 2

def _walk(x, y):
  if x < 0 or y < 0:
    return 0
  if x == 0 and y == 0:
    return 1
  return _walk(x - 1, y) + _walk(x, y - 1)

def walk(n):
  return _walk(n, n)

@chrono
def walkb(n):
  return 2 * _walk(n - 1, n)

def _walk_2(x, y, tab):
  if x < 0 or y < 0:
    return 0
  if x == 0 and y == 0:
    return 1
  if tab[x][y] == 0:
    tab[x][y] = _walk_2(x - 1, y, tab) + _walk_2(x, y - 1, tab)
  return tab[x][y]

@chrono
def walkb_2(n):
  table = [ [ 0 for i in range(n+1) ] for j in range(n+1) ]
  return 2 * _walk_2(n - 1, n, table)

def wrap(n):
  print("{} => {} | {}".format(n, walkb(n), walkb_2(n)))

wrap(1)
wrap(2)
wrap(3)
wrap(4)
wrap(5)
wrap(6)

print(walkb_2(20))
