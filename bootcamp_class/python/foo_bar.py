# Foo and Bar
'''
Write a program that prints all the prime numbers and all the perfect squares for all numbers between 100 and 100000.
'''

# print first (example) row
def is_prime(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

n = 100000
p = 100  

def print_prime_numbers():
  for i in range(p, n + 1):
    # determine if i is prime number
    if is_prime(p):
      print "Foo"
    else:
      print "FooBar"

    # determind if i is a perfect square
    # elif i == perfect square:
    #   print "Bar"
    # # if neither, print FooBar
print_prime_numbers()