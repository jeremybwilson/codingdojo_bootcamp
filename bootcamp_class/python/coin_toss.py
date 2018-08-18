# Coin Tosses
# Write a function that simulates tossing a coin 5,000 times. 
# Your function should print how many times the head/tail appears.

# import the random library
import random

def coin_toss_func():
  game_str = ''
  game_str += "Starting the program..."
  x = "tails!"
  y = "heads!"
  x_counter = 0
  y_counter = 0
  
  # define the value range from 1 to 101
  for value in range(1,101):
    # use built in random method to generate heads/tails
    toss =  str(random.choice([x, y]))
    # create a string that shows attempt number and heads/tails toss dynamically
    game_str += "Attempt #"+str(value)+": Throwing a coin... It's a "+toss
    
    if toss == x:
      x_counter += 1
      game_str += "... Got "+str(x_counter)+" tail(s) so far and "+str(y_counter)+" head(s) so far\n"
    else:
      y_counter += 1
      game_str += "... Got "+str(y_counter)+" head(s) so far and "+str(x_counter)+" tail(s) so far\n"
  
  game_str += "Ending the program, thank you!"

  print game_str
coin_toss_func()
