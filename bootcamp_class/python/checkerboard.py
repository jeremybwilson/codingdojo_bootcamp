# Checkerboard
# Write a program that prints a 'checkerboard' pattern to the console.

# define the function
def checkerboard():
  # determine range or number of rows to print
  for i in range(0, 8):
    # determine even rows
    if i%2 == 0:
      # print out checkerboard for even rows
      print "* " * 4
    # all non even rows
    else:
      # print out checkerboard for odd rows
      print " *" * 4

# execute function => print statement not needed
checkerboard()