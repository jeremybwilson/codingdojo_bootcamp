# Multiples
# Part I - Write code that prints all the odd numbers from 1 to 1000. 
# Use the for loop and don't use a list to do this exercise.

def print_0_to_1000():
  # define range from 1 to 1000
  for i in range(1, 1000):
    print i

# excecute the function
print_0_to_1000()

# Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.
def print_multiples_5():

  # define range from 5 to 1,000,000, in multiples of 5
  for i in range(5,1000005,5):
    print i

# excecute the function
# print_multiples_5()

# Sum List
# Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
a = [1, 2, 5, 10, 255, 3]

def sum_list_values(someList):

  # summed_list_values = sum(someList)
  # print "The sum of the list values is: ", summed_list_values

  # define sum/total variable to start at zero
  sum = 0

  for i in a:
    sum += i

  print "The sum of the list values is: ", sum

sum_list_values(a)

# Average List
# Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
a = [1, 2, 5, 10, 255, 3]

def sum_list_values(someList):

  # determine the list length
  list_length = len(someList)
  print  "The list length is: ", list_length

  #determine the sum total of all the list values
  summed_list_values = sum(someList)
  print  "The sum of the list values is: ", summed_list_values

  averaged_list_value = summed_list_values / list_length
  print  "The average value is: ", averaged_list_value

sum_list_values(a)