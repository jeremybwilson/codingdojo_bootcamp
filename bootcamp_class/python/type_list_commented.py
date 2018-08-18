# Type List
# Write a program that takes a list and prints a message for each element in the list, based on that element's data type.

mixed_list = ['magical unicorns',19,'hello',98.98,'world']
integer_list = [2,3,1,7,4,12]
string_list = ['magical','unicorns']

# define a function to take a list as an argument
def identify_list_type(lst):
  # define an empty placeholder string
  new_string = ''
  # define an empty variable for total (int)
  sum = 0

  # loop through values of the provided list
  for value in lst:

    # determine if value is a regular int or a float and if so, add up values
    if isinstance(value, int) or isinstance(value, float):
      # add up int or float values
      sum += value
    # otherwise values must be strings
    elif isinstance(value, str):
      # while looping, add values to new_string (string) variable
      new_string += value

  # if list contains both strings and numbers
  if new_string and sum:
    print "The list you entered is of mixed type"
    print "String: magical unicorns hello world"
    print "Total:", sum

  # or if only a list with string values
  elif new_string:
    print "The list you entered is of string type"
    print "String: magical unicorns"

  # else, this is a list with only numbers
  else:
    print "The list you entered is of integer type"
    print "Sum:", sum

print identify_list_type(mixed_list)
print identify_list_type(integer_list)
print identify_list_type(string_list)



mixed_list2 = ['magical unicorns', 19, 'hello', 98.98, 'world']
integer_list2 = [2,3,1,7,4,12]
string_list2 = ['magical', 'unicorns']

def find_list_type(someList):

  total = 0
  my_string = ""
  output_type = ""

  for item in someList:
    if isinstance(item, int):
      total += item
        
      if output_type == "string":
       output_type = "mixed"

      else:
        output_type = "number"

    elif isinstance(item, str):
      my_string += item

      if output_type == "number":
        output_type = "mixed"

      else:
        output_type = "string"

print find_list_type(mixed_list2)
print find_list_type(integer_list2)
print find_list_type(string_list2)
