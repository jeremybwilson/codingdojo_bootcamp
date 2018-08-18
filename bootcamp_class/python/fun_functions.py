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
  for i in range(1,2000):

    if(i % 2 == 0):
      print "Number is", i, "This is an even number."

    else:
      print "Number is", i, "This is an odd number."

# odds_evens_func()

# 2. Multiply:
# Create a function called 'multiply' that iterates through each value in a list 
# (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.


def multiply_func(some_array, num):

  for x in range(0, len(some_array)):
    some_array[x] *= num
  
  return some_array

a = [2, 4, 10, 16]
b = multiply_func(a, 5)
print "Here is the output of the variable b: ", b

# a = [2, 4, 10, 16]
# b = multiply_func(a, 5)
# print "The results are:", b


# 3. Hacker Challenge:
# Write a function that takes the multiply function call as an argument. 

def layered_multiples(arr):
  # print arr
  print arr
  new_array = []

  for x in arr:
    val_arr = []
    for i in range(0, x):
      val_arr.append(1)
    new_array.append(val_arr)
  return new_array

x = layered_multiples(multiply_func([2,4,5],3))
print x

