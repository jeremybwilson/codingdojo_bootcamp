# Type List
# Write a program that takes a list and prints a message for each element in the list, 
# based on that element's data type.

mixed_list = ['magical unicorns',19,'hello',98.98,'world']
integer_list = [2,3,1,7,4,12]
string_list = ['magical','unicorns']

def identify_list_type(lst):
  new_string = ''
  total = 0

  for value in lst:

    if isinstance(value, int) or isinstance(value, float):
      total += value
    elif isinstance(value, str):
      new_string += value

  if new_string and total:
    print "The list you entered is of mixed type"
    print "String: magical unicorns hello world"
    print "Total:", total

  elif new_string:
    print "The list you entered is of string type"
    print "String: magical unicorns"

  else:
    print "The list you entered is of integer type"
    print "Total:", total

print identify_list_type(mixed_list)
# output for mixed list
# "The list you entered is of mixed type"
# "String: magical unicorns hello world"
# "Sum: 117.98"

print identify_list_type(integer_list)
# output for integer list
# "The list you entered is of integer type"
# "Sum: 29"

# output for string list
# "The list you entered is of string type"
# "String: magical unicorns"c
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
