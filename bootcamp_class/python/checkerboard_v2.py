# Checkerboard
# Write a program that prints a 'checkerboard' pattern to the console.

# define the function
def checkerboard(x, y):
  # define variables for rows and cols
  rows = 0
  columns = 0
  # determine range or number of rows to print
  for i in range(0, y):
    # determine even rows
    if i%2 == 0:
      # print out checkerboard for even rows
      print "* " * x
    # all non even rows
    else:
      # print out checkerboard for odd rows
      print " *" * x

# execute function => print statement not needed
checkerboard(10, 8)