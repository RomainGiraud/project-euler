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

def cl(s):
  count = 0
  for s in s:
    if s != ' ' and s != '-':
      count += 1
  return count

tab = {
  0: 'zero',
  1: 'one',
  2: 'two',
  3: 'three',
  4: 'four',
  5: 'five',
  6: 'six',
  7: 'seven',
  8: 'eight',
  9: 'nine',
  10: 'ten',
  11: 'eleven',
  12: 'twelve',
  13: 'thirteen',
  14: 'fourteen',
  15: 'fifteen',
  16: 'sixteen',
  17: 'seventeen',
  18: 'eighteen',
  19: 'nineteen',
  20: 'twenty',
  30: 'thirty',
  40: 'forty',
  50: 'fifty',
  60: 'sixty',
  70: 'seventy',
  80: 'eighty',
  90: 'ninety',
}

def int2str(n):
  n = int(n)
  s = str(n)
  if len(s) == 3:
    c = int(s[0])
    l = s[1:3]
    if int(l) == 0:
      return "{0} hundred".format(int2str(c))
    return "{0} hundred and {1}".format(int2str(c), int2str(l))
  elif len(s) == 2:
    if n in tab:
      return tab[n]
    d = int(s[0] + '0')
    l = s[1]
    if int(l) == 0:
      return "{0}".format(tab[d])
    return "{0}-{1}".format(tab[d], int2str(l))
  elif len(s) == 1:
    return tab[n]
  raise BaseException("number too big")

total = 0
for i in range(1, 1000):
  total += cl(int2str(i))
total += cl("one thousand")
print(total)
