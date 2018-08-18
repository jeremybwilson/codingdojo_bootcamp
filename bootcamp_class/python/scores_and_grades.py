# Fun with Functions
# Odd/Even:
# Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print 
# the number of that iteration and specify whether it's an odd or even number.

import random

def scores_and_grades(num):

  # define random number with this variable
  random_num = random.random()
  # print scores and grades title
  print "Scores and Grades"

  # loop through range of 1, 2000
  for i in range(1, 101):
    # define score variable using randomint() method
    score = random.randint(60, 101)

    # cycle through scores from 60 <= 69
    if score >= 60 and score <= 69:
      grade = "D"
      print "Your score is", score, "; Your grade is -", grade

    elif score >= 70 and score <= 79:
      grade = "C"
      print "Your score is", score, "; Your grade is -", grade

    elif score >= 80 and score <= 89:
      grade = "B"
      print "Your score is", score, "; Your grade is -", grade

    elif score >= 90 and score <= 100:
      grade = "A"
      print "Your score is", score, "; Your grade is -", grade

    else:
      print "You should study more"

  print "End of the program. Bye!"

# scores_and_grades(10)

def scores_and_grades2(num):
  print "Scores and Grades"
  random_num = random.random()

  for x in range(0, num):

    score = random.randint(60, 101)

    if score >= 60 and score <= 69:
      print "Score:", score, "; Your grade is - D"
    elif score >= 70 and score <= 79:
      print "Score:", score, "; Your grade is - C"
    elif score >= 80 and score <= 89:
      print "Score:", score, "; Your grade is - B"
    elif score >= 90 and score <= 100:
      print "Score:", score, "; Your grade is - A"

    else:
      print "You failed"

  print "End of the program. Bye!"


scores_and_grades2(10)


