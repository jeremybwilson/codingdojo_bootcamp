# Tuples
# A Tuple is a container for a fixed sequence of data objects.

import math

# provided code
tuple_data = ('physics', 'chemistry', 1997, 2000)
tuple_num = (1, 2, 3, 4, 5 )
tuple_letters = "a", "b", "c", "d"

dog = ("Canis Familiaris", "dog", "carnivore", 12)

print dog[2]

# for data in dog:
#   print "Here is the data in dog: ", data

# dog[0] = "X"
#TypeError: 'tuple' object does not support item assignment

dog = dog + ("domestic",)
dog = dog[:3] + ("man's best friend",) + dog[4:]

dog_x = (1,5,6,9,2)
print "Here is a the length of dog_x: ", len(dog_x)
# output: => 5

def get_circle_area(r):
  #Return (circumference, area) of a circle of radius r
  circum = 2 * math.pi * r
  area = math.pi * r * r
  return (circum, area)

print "Circumference and area are: ", get_circle_area(5)

def get_max(sequence):
  max_val = max(sequence)
  return max_val

print get_max(dog_x)

def get_sum(sequence):
  sum = 0

  for vals in sequence:
    sum += vals

  return sum

print get_sum(dog_x)