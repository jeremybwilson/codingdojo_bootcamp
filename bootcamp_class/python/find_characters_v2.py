# Find Characters
# Write a program that takes a list of strings and a string containing a single character, 
# and prints a new list of all the strings containing that character.

# input
word_list = ['hello','world','my','name','is','Anna']
# looking for someValue = 'o'
# output new_list = ['hello','world']

# define the function, using as arguments, a list and a special character to search
def find_special_character(someList, someValue):
    # define an empty list => new_list
    new_list = []
    # find value of index (i) in range of list (from 0 to length of list)
    for i in range(0, len(someList)):
      # if the special character in the index of wordlist does not (!=) equal -1
      if someList[i].find(someValue) != -1:
        # then append index of someList into the new_list (list)
        new_list.append(someList[i])

    # print the list named new_list
    print new_list

# execute the function
find_special_character(word_list, 'o')
# print find_special_character(word_list, 'o')