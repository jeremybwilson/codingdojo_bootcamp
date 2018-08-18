# Type List
# Write a program that takes a list and prints a message for each element in the list, 
# based on that element's data type.

mixed_list1 = ['magical unicorns', 19, 'hello', 98.98, 'world']
integer_list1 = [2,3,1,7,4,12]
string_list1 = ['magical', 'unicorns']

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

print find_list_type(mixed_list1)
print find_list_type(integer_list1)
print find_list_type(string_list1)
