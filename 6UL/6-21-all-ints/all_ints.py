# ------------
# User Instructions
#
# Define a function, all_ints(), that generates the 
# integers in the order 0, +1, -1, +2, -2, ...

def all_ints():
    "Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
    # Your code here.
    i = 0
    j = 0
    yield i
    while True:
        i += 1
        yield i
        j -= 1
        yield j

if __name__ == "__main__":
  for i in all_ints():
    print(i)
