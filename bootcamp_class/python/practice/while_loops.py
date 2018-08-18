# Python program to illustrate
# while loops



# Structure of a while loop
# count = 0;
# while <expression>: # notice the colon
  # do something => print 'looping - ', count
  # count += 1

my_list = [4,'dog',99,['list','inside','another'], 'hello world']
count = 0;

while count < len(my_list):
  print 'looping - ', count
  count += 1


# a = 3
# b = a
# while b > 0:
#   print b
#   b = b - 1
# else:
#   print "Final else statement"

# x = 3
# y = x
# while y > 0:
#   print y
#   y = y - 1
#   if y == 0:
#     break
# else:
#  print "Final else statement"

x = '1'
y = 2;
# print int(x) + y
# print str(x) + str(y)
# print x + y  # this line will break the code, cannot concatenate string and an integer