# Find Characters
'''
Write a program that takes a list of strings and a string containing a single character, 
and prints a new list of all the strings containing that character.
'''
# input
word_list = ['hello','world','my','name','is','Anna']
# char = 'o'
# output => new_list = ['hello','world']

def find_characters(someList, someValue):
  newList = []

  for i in range(0, len(someList)):
    if someList[i].find(someValue) != -1:
      newList.append(someList[i])
  return newList

print find_characters(word_list, 'o')