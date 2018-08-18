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

  # new_combined_list = list_back_half.append(list_front_half)
  new_combined_list = list_back_half + list_front_half
  print "The rebuilt list is: ", new_combined_list

new_split_list(list_vals)