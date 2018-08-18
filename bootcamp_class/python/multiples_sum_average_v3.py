# Multiples, Sum, Average

'''
This assignment has several parts. All of your code should be in one file that is well commented 
to indicate what each block of code is doing and which problem you are solving. Don't forget to test your code as you go!
'''

# multiples

def print_odd_nums(multiples):
  for count in range(1, 1001, multiples):
    # return count
    print count

# print print_odd_nums(2)
print_odd_nums(2)

def print_multiples(multiples):
  for count in range(5, 1000, multiples):
    # return count
    print count

# print print_multiples(5)
print_multiples(5)

my_numbers = [1, 2, 5, 10, 255, 3]

def sum_list(someList):
  count = 0
  for i in someList:
    count += i
  return count

print sum_list(my_numbers)

def find_average(someList):
  sum = 0
  for i in someList:
    sum += i
  
  return sum/len(someList)

print find_average(my_numbers)