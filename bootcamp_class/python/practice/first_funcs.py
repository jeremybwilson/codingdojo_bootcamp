# my_func():

def my_func(val):
  print(type(val))
  if isinstance(val, str) == True:
    print('It\'s a string')
  else:
    print("It's something else.")

my_func("hi")
my_func(8)