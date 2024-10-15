#!/usr/bin/env python3

def poker(hand):
  """
  >>> True
  True
  """
  return ???

def poker(hands):
  "Return the best hand: poker([hand,...]) => hand"
  return max(hands, key=hand_rank)

def test():
  "Test cases for the functions in poker program"
  sf = "6C 7C 8C 9C TC".split()  # => ['6C', '7C', '8C', '9C', 'TC']
  fk = "9D 9H 9S 9C 7D".split()
  fh = "TD TC TH 7C 7D".split()
  assert poker([sf, fk, fh]) == sf
  print("sf test passed")
  assert poker([fk, fh]) == fk
  print("fk test passed")
  assert poker([fh, fh]) == fh
  print("fh test passed")

def hand_rank(hand):
  return None
  

if __name__ == "__main__":
  import doctest
  doctest.testmod()
