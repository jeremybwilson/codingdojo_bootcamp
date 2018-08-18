# define a function that says hello to the name provided
# this starts a new block
first_name = "Jeremy"
last_name = "Wilson"
name_number = 10

#print "My name is {} {}".format(first_name, last_name)
full_name = first_name + " " + last_name
number = 10
# cannot concatenate strings and ints
# full_name = first_name + name_number
print "My name is", full_name
print "My name is " + full_name

print "My name is", number
print "My name is " + str(number)

string = "this is string example....wow!!!";
sub = "i"
print "string.count(sub, 4,40) : ", string.count(sub, 4, 40)
print "string.endswith('wow') : ", string.endswith('wow')
print "string.find('wow') : ", string.find('wow')

sub = "wow"
print "string.count.count(sub) : ", string.count(sub)

string = "abc123";
print "The string is alpha-numeric: ", string.isalpha()

string = u"123456";
print "The string is numeric: ", string.isnumeric()

string = " "
list = ["jeremy","is","learning","to","code"];
print "string.join(list) : ", string.join(list)

sub = " "
string = "jeremy is learning to code"
print "string.split(string) : ", string.split(sub)

hw = "hello %s" % 'world'
print hw.upper()

# the output would be:
# hello world

def say_hello(name):
  # name = 'Jeremy'
  #these lines are indented therefore part of the function
  if name:
   print 'Hello, ' + name + ' from inside the function'
  else:
   print 'No name'
# now we're unindented and have ended the previous block
print 'Outside of the function'

print say_hello('Jeremy')