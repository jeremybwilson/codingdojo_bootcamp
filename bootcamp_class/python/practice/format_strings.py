# Strings are any sequence of characters (letters, numerals, 
# ~($/}\#, etc.) enclosed in single or double quotes. 
# You can display a string like this:

# using triple quotes
# print('''He said, "What's there?"''')

# escaping single quotes
# print('He said, "What\'s there?"')

# escaping double quotes
# print("He said, \"What's there?\"")

# default(implicit) order
default_order = "{}, {} and {}".format('John','Bill','Sean')
# print('\n--- Default Order ---')
# print(default_order)

# order using positional argument
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
# print('\n--- Positional Order ---')
# print(positional_order)

# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
# print('\n--- Keyword Order ---')
# print(keyword_order)

first_name = "Jeremy"
last_name = "Wilson"
print "My name is {} {}".format(first_name, last_name)

str1 = 'Bojack Horseman'
str2 = 'jack'
print str1.find(str2)

x = "Hello World"
print x.upper()
# output: "HELLO WORLD"

print 'Is x an digit/integer: ', x.isdigit()