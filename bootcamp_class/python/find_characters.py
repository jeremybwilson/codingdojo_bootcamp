# Find Characters
# Write a program that takes a list of strings and a string containing a single character, 
# and prints a new list of all the strings containing that character.

# input
word_list = ['hello','world','my','name','is','Anna']
# looking for char = 'o'
# output new_list = ['hello','world']

# define the function, using as arguments, a list and a special character to search
def find_characters(someList, character):
    # define an empty new_list (list)
    new_list = []
    # find value of index (i) in range of list (from 0 to length of list)
    for i in range(0, len(word_list)):
      # if index of word_list != to -1
      if word_list[i].find(character) != -1:
        # then append index of wordlest into the new_list (list)
        new_list.append(word_list[i])
    # print the list named new_list
    print "Here is the new list with the searched character: ", new_list

print find_characters(word_list, 'o')