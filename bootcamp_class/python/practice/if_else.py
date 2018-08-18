# Python program to illustrate
# if else statements

# age = 18;
# if age >= 18:
#   print 'You are of legal age'
# else:
#   print 'You are so young!'

# age = 21;
# if age >= 18:
#   print 'Legal age'
# elif age == 17:
#   print 'You are seventeen.'
# else:
#   print 'You are so young!'


# Debugging with Minh
# Example 1

# my_list = [41,23]
# my_second_list = [
# 42,
# 24
# ]

# try:
#     print "hello"
#     print my_list[1] + my_second_list[2]
#     print "hello"
#     print "hello"
# except IndexError:
#   print my_list[0] + my_second_list[1]
# except IndentationError:
#   print "Indentation error"
# except KeyError:
#   print "Key error"
# except TypeError:
#   print "Type error"
# except:
#   print "nonononooo"

# Example 2
# using parantheses to clearly mark a tuple
# num = (14, 17, 42)
# print num
# num1, num2, num3 = 1, 3, 5
# print (num2)

# Example 3
#  
## i, j = 1,2   # causes an error 'too many values to unpack'
# i,j,k = 1,2,3
# print (i,j,k)
## (i,j) = (1,2,3)  #  causes an error 'not enough values to unpack'
# (i,j,k) = (1,2,3)
# print (i,j,k)


# Example 4
our_list = ['Alex','Anika','Jeremy']
# print enumerate(our_list)   # [(0, 'Alex'),(1, 'Anika'), (2, 'Jeremy')]
# for i in range(0, len(our_list)):
#   print i

# for val in enumerate(our_list):
#   print val

# for idx,value in enumerate(our_list):
#   print value, idx

jeremy = {
  "first_name":"Jeremy",
  "last_name":"Wilson",
  "age":"27",
  "hobbies":["coding","skiing"]
}
# for val in jeremy:
#   print val

key, value = "AP"
print key, value
