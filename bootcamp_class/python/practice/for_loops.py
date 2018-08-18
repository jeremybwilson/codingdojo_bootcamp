# Python program to illustrate
# for loops

jeremy = {
  "first_name": "Jeremy",
  "last_name": "Wilson"
}
alex = {
  "first_name": "Alex",
  "last_name": "Wilson"
}

# Structure of a for loop
# for <counter> in <sequence or range>:
  # do something

# for count in range(0, 5):
#   print "looping - ", count

# create a new list
# remember lists can hold many data-types, even lists
my_list = [4,'dog',99,['list','inside','another'], 'hello world']

def iterate_list():

  # for element in my_list:
  #   print element

  count = 0
  while count < 5: 
    print "looping - ", count
    count += 1

iterate_list()

def using_break_statement():

  for val in "string of text":
    if val == "e":
      break
    print val
    
using_break_statement()

# # for key in jeremy:
#   # print key
#   # print jeremy[key]

myList = [5,3,7,2]

# for i in myList:
# for i in range(0, 50):
#   print "hello" + str(i)
# print "goodbye"

# for value in myList:
#   print value
# print "goodbye"

myList2 = [jeremy,alex]

# for value in range(0, len(myList), 2):  # adding 2 allows the ability to increment by 2
#   print value
# print myList
# print "goodbye"

# for key in jeremy:
#   print key
#   print jeremy[key]

# for value in myList2: # 0-4
#   print value
#   for key in value:
#     print value[key]
    
  # print myList2[value]  # prints each value in the list
  # myList2[value] = 5  # changes all values to 5 

# print myList 
# print "goodbye"