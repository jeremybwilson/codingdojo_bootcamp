# Debugging
# Try running the code examples below to get the most out of this lesson.

# provided code
def multiply(arr, num):
  for x in arr:
      x *= num
  # print arr
  return arr
a = [2,4,10,16]
b = multiply(a,5)
# print b
print multiply(a, 5)
# output: => [2,4,10,16]


# def multiply(arr,num): #don't go inside the function until the function is called
# a = [2,4,10,16]
# b = multiply(a,5)     # now our function executes; what is a function call equal to?
# print b               # and the resulting value is printed

# Here's what happened, in order:
# declare a function
# instantiate a variable whose value is a list containing integers
# print the output of that function by calling it after a print statement

def multiply2(arr,num):
  # print arr, num        # output should be [2,4,10,16] 5
  for x in range(len(arr)):
    arr[x] = arr[x] * num
  # print arr
  return arr
a = [2,4,10,16]
b = multiply2(a,5)
print b
