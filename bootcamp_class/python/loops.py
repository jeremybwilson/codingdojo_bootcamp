# Loops

# create a new list
# remember lists can hold many data-types, even lists!

x = ['list', 'inside', 'another']
my_list = [4, 'dog', 99, ['list', 'inside','another'], 'hello world!']

for element in my_list:
  print element

for count in range(0, 5):
  print "looping - ", count

count = 0
while count < 5:
  print 'looping with while - ', count
  count += 1