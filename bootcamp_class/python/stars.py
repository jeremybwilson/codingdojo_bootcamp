# Stars
# Write the following functions.
# Part I
'''
Create a function called draw_stars() that takes 
a list of numbers and prints out *.
'''

x = [4, 6, 1, 3, 5, 7, 25]

def draw_stars(arr):

  for values in arr:

    print "*" * values

draw_stars(x)

# Part II
'''
Modify the function above. Allow a list containing integers 
and strings to be passed to the draw_stars() function.
'''

x = [4, "Jeremy", 1, "Wilson", 5, 7, "Gordon Wilson"]

def draw_stars_2(arr):

  for x in arr:
    if isinstance(x, int):
      print "*" * x

    elif isinstance(x, str):
      length = len(x)
      letter = x[0].lower()
      print letter * length

draw_stars_2(x)