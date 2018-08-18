# Stars
# Write the following functions.

# 1. Create a function called draw_stars() that takes a list of numbers and prints out *.

x = [4, 6, 1, 3, 5, 7, 25]

def draw_stars(arr):

  for vals in arr:

    stars = "*" * vals
    print stars

  # return stars

draw_stars(x)

# 2. Modify the function above. Allow a list containing integers 
# and strings to be passed to the draw_stars() function.

x = [4, "Jeremy", 1, "Wilson", 5, 7, "Gordon Wilson"]

def draw_stars_2(arr):
  # loop through the list values
  for vals in arr:
    # if the instance is an int
    if isinstance(vals, int):
      # print * symbol as many times as the value of vals
      print "*" * vals

    elif isinstance(vals, str):
      # length is equal to length of the vals list
      length = len(vals)
      # letter variable is equal to the first value of each vals, lowercased
      letter = vals[0].lower()
      # print letter * length
      print letter * length

draw_stars_2(x)