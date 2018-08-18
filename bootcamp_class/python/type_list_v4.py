# Type List
# Write a program that takes a list and prints a message for each element in the list, 
# based on that element's data type.

mixed_list2 = ['magical unicorns', 19, 'hello', 98.98, 'world']
integer_list2 = [2,3,1,7,4,12]
string_list2 = ['magical', 'unicorns']

def find_list_type2(someList):

  length = len(someList)    # length of list
  count = 0
  sum = 0
  string = ""
  num = 0

  while count<length:
    if type(someList[0]) != type(someList[count]):
      num += 1    #we can check how many different datatypes are in list
    else:
      num == 0
    if isinstance(someList[count] , int) or isinstance(someList[count] , float):
      sum += someList[count]
    elif isinstance(someList[count],str):
      string += someList[count]+" "
    count += 1

  if num > 0:
    print "The list you entered is of mixed type"
    print "String :", string
    print "Sum :", sum
  else:
    if type(someList[0]) == int:
      print "The list you entered is of Integer type"
      print "Sum :", sum
    elif type(someList[0]) == str:
       print "The list you entered is of String type"
       print "String :", string

print find_list_type2(mixed_list2)
print find_list_type2(integer_list2)
print find_list_type2(string_list2)
