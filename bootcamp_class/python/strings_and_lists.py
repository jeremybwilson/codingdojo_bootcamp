# print the position of the first instance of the word "day". 
# Then create a new string where the word "day" is replaced with the word "month".

words = "It's thanksgiving day. It's my birthday,too!"
obj1 = "day"
obj2 = "month"

# print words.find(obj1)
# print words.replace(obj1, obj2)

def find_first_instance():

  # print the position of the first instance of the word "day". 
  somevalue = words.find(obj1);
  # replace word day with the word month

  print words.replace(obj1, obj2)
  # Print the min and max values in a list.

print find_first_instance()



































list_vals = [2,54,-2,7,12,98]

def max_min_function(someList):

  # sort the list 
  results_list = sorted(someList)
  print "Here is the list sorted: ", results_list

  # find the length of the list
  list_length = len(someList)
  # print the len of the list
  print "The list length is: ", list_length

  # loop through values in list_vals

  # find the min value
  # min_value = min(someList)   # not using built-in for find max value
  min_value = results_list[0]      # pulling last value in the overall length of the list

  # print the min value
  print "Min value element : ", min_value

  # find the max value
  # max_value = max(someList)  # not using built-in for find max value
  # max_value = results_list[-1]      # pulling last value in the overall length of the list
  max_value = results_list[len(results_list) - 1]  # JS way of determine final index of list (array)

  # print the min value
  print "Max value element : ", max_value

max_min_function(list_vals)

# Print the first and last values in a list like this one:
# Now create a new list containing only the first and last values in the original list. Your code should work for any list.

list_vals = ["hello",2,54,-2,7,12,98,"world"]

def first_and_last_values(someList):

  # sorting this particular list is unnecessary
  # results_list = sorted(someList)
  # print "Here is the list sorted: ", results_list

  # find the first value
  # first_value = find(someList)
  first_value = someList[0]

  # print the first value
  print "First element : ", first_value

  # find the last value
  # last_value = find(someList)
  last_value = someList[-1]

  # print the last value
  print "Last element : ", last_value

first_and_last_values(list_vals)


# Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. 
# Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. 
# The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!

list_vals = [19,2,54,-2,7,12,98,32,10,-3,6]

def new_split_list(someList):

  # sort the list 
  results_list = sorted(someList)
  print "Here is the list sorted: ", results_list

  # find the length of the list
  list_length = len(results_list)
  print "The list length is: ", list_length

  # divide the list by 2 at the halfway point

  # define the first half
  list_front_half = results_list[:len(results_list) / 2]
  print "The first half of the list is: ", list_front_half

  # define the back half of the list
  list_back_half = results_list[len(results_list) / 2:]
  print "The second half of the list is: ", list_back_half

  # new_combined_list = list_back_half.append(list_front_half).   # .append() is not working here
  # new_combined_list = list_back_half + list_front_half          # this works to combine lists but is not what the assignment asks for
  # print "The rebuilt list is: ", new_combined_list
  list_back_half.insert(0,list_front_half)
  print "The rebuilt list is: ", list_back_half

new_split_list(list_vals)