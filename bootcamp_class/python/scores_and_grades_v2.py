# Scores and Grades
'''
Write a function that generates ten scores between 60 and 100. 
Each time a score is generated, your function should display what the grade is for a particular score. 
Here is the grade table:
'''
# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A
import random

def scores_and_grades(num):
  # define an empty list for score values
  scores_array = []
  # scores = 0
  # create random score values between 60 and 100, 10 total
  # total number determined by parameter => num
  for i in range(0, num):
    scores = random.randint(60, 100)
    # push (append) each score to a list
    scores_array.append(scores)
    # return the new array
  
  print "Here is the array of randomly generated scores: ", scores_array

  for vals in scores_array:
    # elif vals >= 60 and vals <= 79:
    if vals in range(60, 70):
      letter_grade = 'D'
      print "Score: {}; Your grade is {}".format(vals, str(letter_grade))

    elif vals in range(70, 80):
    # elif vals >= 70 and vals <= 79:
      letter_grade = 'C'
      print "Score: {}; Your grade is {}".format(vals, str(letter_grade))

    elif vals in range(80, 90):
    # elif vals >= 80 and vals <= 89:
      letter_grade = 'B'
      print "Score: {}; Your grade is {}".format(vals, str(letter_grade))

    elif vals in range(90, 101):
    # elif vals >= 90 and vals <= 100:
      letter_grade = 'A'
      print "Score: {}; Your grade is {}".format(vals, str(letter_grade))
    else:
      print "Your scores was: ", vals, "You failed."

print scores_and_grades(20)
