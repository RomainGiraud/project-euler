#!/usr/bin/env python

'''
1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
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

def is_leap(year):
  return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def get_days(month, year):
  if month == 1:
    return months[month] + (1 if is_leap(year) else 0)
  return months[month]


total_sundays = 0
first_day = (0 + 365) % 7
for y in range(1901, 2001):
  for m in range(0, 12):
    if first_day == 6:
      total_sundays += 1
    first_day = (first_day + get_days(m, y)) % 7
print(total_sundays)





total_sundays = 0
basic_year = 30 * 4 + 31 * 7 + 28
first_day = (0 + basic_year + (1 if is_leap(1900) else 0)) % 7
for i in range(1901, 2001):
  nb = (basic_year + (1 if is_leap(i) else 0))
  c = (int)(nb / 7)
  if first_day <= 6 and 6 < first_day + (nb - c * 7):
    c += 1
  #print("{0}({1}): {2} / {3}".format(i, first_day, c, nb))
  total_sundays += c
  first_day = (nb + first_day) % 7
#print(total_sundays)
