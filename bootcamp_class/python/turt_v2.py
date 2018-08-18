# Python Turtle
# Try drawing a simple picture using the Python module Turtle.  
# This will also generate a GUI window showing image being drawn out.

# try this either as a .py file or in the python shell
import turtle

# define a function for turtle drawing
def draw_using_turtle():
  window = turtle.Screen()
  window.bgcolor('white')
  
  # the distance we want the pointer to travel each time
  DISTANCE = 100
  # define value for x with range of O to 6
  for x in range(0, 6):
    # print the value of x
    print "x", x
    for y in range(1, 5):
      print "y", y
      # turn the pointer 90 degrees to the right
      turtle.right(90)
      # advance according to set distance
      turtle.forward(DISTANCE)
    # add to set distance
    DISTANCE += 20

draw_using_turtle()