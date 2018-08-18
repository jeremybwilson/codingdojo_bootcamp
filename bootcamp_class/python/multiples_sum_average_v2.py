# Multiples, Sum, Average

# Multiples
# Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.

def multiples1():

  for i in range(1, 1000):

    if(i%2 != 0):
      print i

print multiples1()

# Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.
def multiples2():
  # loop through range using two arguments, starting and ending values
  for x in range(5, 1000005):
    # use modulo to determine value divisable by 5
    if(x%5 == 0):
      print x

print multiples2()

# another version
def multiples3():
  # loop through range using three arguments including 5 multiple
  for x in range(5, 1000005, 5):
      print x

print multiples3()

# Sum List
# Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
a = [1, 2, 5, 10, 255, 3]
def find_sum(arr):

  sum = 0

  for x in arr:

    sum += x

  return sum

print find_sum(a)

# Average List
# Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
a = [1, 2, 5, 10, 255, 3]
def find_average(arr):
  # define empty total variale for later math to find average
  total = 0

  for x in arr:
    total += x
  
  return total / len(arr)

print "The average value is", find_average(a)




