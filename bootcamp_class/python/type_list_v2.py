# Type List
# Write a program that takes a list and prints a message for each element in the list, based on that element's data type.

mixed_list = ['magical unicorns',19,'hello',98.98,'world']
integer_list = [2,3,1,7,4,12]
string_list = ['magical','unicorns']

# define a function to take a list as an argument
def identify_list_type(lst):
  # define an empty variable for total (int)
  sum = 0
  # define an empty placeholder string
  T = ''
  # define an isstring Boolean
  isstring = False;
  # define an isint Boolean
  isint = False;

  # loop through values of the provided list
  for i in range(0, len(lst)):

    # determine if list indexes contain strings and or ints/floats
    if(type(lst[i]) == str or int or float):

      # determine if value is a string
      if(type(lst[i]) == str):
        T = T + " " + lst[i]
        isstring = True

      # determine if value is a regular int or a float and if so, add up values
      elif(type(lst[i]) == int or float):
        sum = sum + lst[i]
        isint = True

  # if list contains both strings and numbers
  if(isstring and isint):
    print "It's a mixed array"
  # or if only a list with string values
  elif(isstring):
    print "String:", str(T)

  # else, this is a list with only numbers
  elif(isint):
    print "Sum:", str(sum)

  else:
    pass

print identify_list_type(mixed_list)
print identify_list_type(integer_list)
print identify_list_type(string_list)

