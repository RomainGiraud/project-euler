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

def clean(s):
  s = s.strip()
  return s[1:len(s)-1]

file = open("p022_names.txt", "r")
tab = file.read().split(',')
tab[:] = map(clean, tab)
tab.sort()
print("#{0}#".format(tab[937]))
print("#{0}#".format(tab[0]))

sum = 0
for k,v in enumerate(tab):
  c = 0
  for j in v:
    if ord('A') <= ord(j) and ord(j) <= ord('Z'):
      c += ord(j.upper()) - ord('A') + 1
    else:
      print("ERROR: #{0}# {1} {2}".format(j, k, v))

  if c <= 0:
    print("ERROR")

  if v == "COLIN":
    print("{0} * {1} = {2}".format(c, k + 1, c * (k + 1)))

  sum += (c * (k + 1))

print(sum)
