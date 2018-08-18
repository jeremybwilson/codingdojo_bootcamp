# Coin Tosses
'''
1. Write a function that simulates tossing a coin 5,000 times. 
Your function should print how many times the head/tail appears.
'''
# import the random library
import random

# define the function => no argument needs to be passed
def coin_toss_func():
  # define empty string for game_str
  game_str = ''
  # append or change game_str to the following text => "Starting the program..."
  game_str += 'Starting the program...'
  # define heads/tails variables with string values for 'heads' or 'tails'
  x = 'tails!'
  y = 'heads!'
  # define counter variables for tails (x) and heads (y)
  x_counter = 0
  y_counter = 0
  
  # define the value range from 1 to 101
  for vals in range(0, 101):
    # use built in random method to generate heads/tails
    toss = str(random.choice([x, y]))
    # create a string that shows attempt number and heads/tails toss dynamically
    game_str += 'Attempt number #' + str(vals) + ' Throwing a coin... It\'s a ' + str(toss) + ' '
    # print toss
    
    
    # if toss is equal to x
    if toss == x:
      # increment x_counter by 1
      x_counter += 1
      # create game_str so it includes count vaue for heads and or tails so far
      print x_counter
      game_str += 'Got ' + str(y_counter) + ' ' + str(toss) + '(s) so far and ' + str(x_counter) + ' tails so far \n'
    
    # otherwise toss is equal to y
    else:
      # increment y_counter by 1
      y_counter += 1
      # create game_str so it includes count vaue for heads and or tails so far
      game_str += 'Got ' + str(x_counter) + ' ' + str(toss) + "(s) so far and " + str(y_counter) + ' heads so far \n'
      print y_counter

  # append game_str value with closure line/verbiage
  game_str += 'Ending the program, thank you!'
  # print game_str
  return game_str

print coin_toss_func()
