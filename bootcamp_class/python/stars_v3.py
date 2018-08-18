# Part I
'''Create a function called draw_stars() that takes 
a list of numbers and prints out *.'''

array_1 = [2,4,3,6,4,7,10]

def draw_stars(arr):

  for vals in arr:

    print "*" * vals

draw_stars(array_1)

# Part II
'''
Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. 
When a string is passed, instead of displaying *, you may use the .lower() string method for this part.
'''
array_2 = [4, "Jeremy", 1, "Wilson", 5, 7, "Gordon Wilson"]

def draw_stars_letters(arr):

  for vals in arr:
    if isinstance(vals, int):
      print '*' * vals

    elif isinstance(vals, str):
      length = len(vals)
      letter = vals[0].lower()
      print letter * length

draw_stars_letters(array_2)