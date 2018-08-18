# Compare List
# Write a program that compares two lists and prints a message 
# depending on if the inputs are identical or not.

list_1 = [1,2,5,6,2]
list_2 = [1,2,5,6,2]

list_3 = [1,2,5,6,5]
list_4 = [1,2,5,6,5,3]

list_5 = [1,2,5,6,5,16]
list_6 = [1,2,5,6,5]

list_7 = ['celery','carrots','bread','milk']
list_8 = ['celery','carrots','bread','cream']

def compare_lists(list_one, list_two):
  if list_one == list_two:
    print "The lists are the same"
  else:
    print "The lists are not the same"

print compare_lists(list_1, list_2)
print compare_lists(list_3, list_4)
print compare_lists(list_5, list_6)
print compare_lists(list_7, list_8)