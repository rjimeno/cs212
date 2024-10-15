#!/usr/bin/env python3

def ints(start, end = None):
    i = start
    while end is None or i <= end:  # Inverted evaluation order for Python3.
        yield i
        i = i + 1

if __name__ == "__main__":
  print("The positive natural numbers in the interval [10, 20] are:")
  for i in ints(10, 20):
    print(i)
  print("From that point onwards:")
  for i in ints(21):
    print(i)
