#!/usr/bin/env python3

import itertools
import time

def try1():
  for odd in range(511, 999, 2):
    even = str(odd + odd)
    odd = str(odd)
    if odd[1] != odd[2]:
      continue
    if int(odd[0]) + int(odd[0]) + 1 != int(even[0:2]):
      continue
    if even[2] == "1":
      print(f"{odd} + {odd} == {even}")

# -------------
# User Instructions
#
# Write a function, solve(formula) that solves cryptarithmetic puzzles.
# The input should be a formula like 'ODD + ODD == EVEN', and the 
# output should be a string with the digits filled in, or None if the
# problem is not solvable.
#
# Note that you will not be able to run your code yet since the 
# program is incomplete. Please SUBMIT to see if you are correct.

def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    for f in fill_in(formula):
        if valid(f):
            return f
    return None

def fill_in(formula):
  letters = ''.join(sorted([c for c in set(formula) if c.isupper()]))  # should be a string
  for digits in itertools.permutations('1234567890', len(letters)):
      table = str.maketrans(letters, ''.join(digits))
      yield formula.translate(table)
 
# assume: def fill_in(formula):
#        "Generate all possible fillings-in of letters in formula with digits."
    
def valid(f) -> bool:
  try:
    return eval(f)
  except:
    return False

if __name__ == "__main__":
  assert(valid("1 + 2 == 3"))
  try1()
  print(solve("ODD + ODD == EVEN"))

# Copied from a previous program:

def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.perf_counter()  # time.clock()
    result = fn(*args)
    t1 = time.perf_counter()  # time.clock()
    return t1-t0, result
