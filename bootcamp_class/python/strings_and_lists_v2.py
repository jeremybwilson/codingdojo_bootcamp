# String and List Practice
'''
Use only the built-in methods and functions from the previous tabs to do the following exercises. 
You will find the following methods and functions useful:
'''

words = "It's thanksgiving day. It's my birthday,too!"

found_word = words.find('day')
print found_word

replaced_str = words.replace('day', 'month')
print replaced_str

# Min and max
x = [2,54,-2,7,12,98]
def find_min(someList):
  return min(someList)

print find_min(x)

def find_max(someList):
  return max(someList)

print find_max(x)

# First and last
x = ["hello",2,54,-2,7,12,98,"world"]
def find_first(someList):
  return someList[0]

print find_first(x)

def find_last(someList):
  return someList[len(someList) - 1]

print find_last(x)

# New list
x = [19,2,54,-2,7,12,98,32,10,-3,6]

def sort_list(someList):
  someList.sort()
  print someList
  first_list = someList[:len(someList)/2]
  second_list = someList[len(someList)/2:]
  return [second_list, first_list]

print sort_list(x)