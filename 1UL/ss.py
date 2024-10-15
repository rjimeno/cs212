#!/usr/bin/env python3

def ss(*argv):
  """
  >>> ss()
  0
  >>> ss(1)
  1
  >>> ss(1, 2)
  3
  """
  s = 0
  for arg in argv:
    s += arg
  return s
  

if __name__ == "__main__":
  import doctest
  doctest.testmod()
