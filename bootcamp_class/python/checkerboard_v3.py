# Checkerboard
# Write a program that prints a 'checkerboard' pattern to the console.

def checkerboard(rows):
  # iterate through range of i through some value (rows)
  for i in range(0, rows):
    # for even rows
    if i % 2 == 0:
      print "* " * 6
    # for odd rows
    else:
      print " *" * 6

checkerboard(8)