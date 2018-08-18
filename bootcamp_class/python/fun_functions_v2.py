# Fun with Functions
# 1. Odd/Even:
# Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print 
# the number of that iteration and specify whether it's an odd or even number.

# Number is 1.  This is an odd number.
# Number is 2.  This is an even number.
# Number is 3.  This is an odd number.
# ...
# Number is 2000.  This is an even number.

def odds_evens_func():
  # specific range of numbers => 1 to 2000
  for i in range(1,100):

    if(i % 2 == 0):
      print "Number is", i, "This is an even number."

    else:
      print "Number is", i, "This is an odd number."

odds_evens_func()

# 2. Multiply:
# Create a function called 'multiply' that iterates through each value in a list 
# (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.


def multiply_func(someList, y):
  # define empty variable for sum
  new_list = []
  # iterate through the list values
  for vals in someList:
    # multiply existing list values against y parameter
    vals = vals * y
    # append new vals to new_list
    new_list.append(vals)
  # return the new_list
  return new_list

a = [2, 4, 10, 16]
b = multiply_func(a, 5)
# print b

# a = [2, 4, 10, 16]
# b = multiply_func(a, 5)
# print "The results are:", b


# 3. Hacker Challenge:
# Write a function that takes the multiply function call as an argument. 

def layered_multiples(arr):
  # your code here
  new_array = []

  # iterate through the list vals
  for i in arr:
    # create empty list to hold new values
    values_array = []

    # iterate through i values in range from 0 to 
    for i in range(0, i):
      # append (insert) the number 1 into the values_array
      values_array.append(1)
    # append the values_array as values of new_array
    new_array.append(values_array)

  return new_array
x = layered_multiples(multiply_func([2,4,5],3))
print x

