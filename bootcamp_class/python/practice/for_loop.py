# For loop practice - 1 to 255

def find_odds_in_range():

  # define for loop to print from range 1 to 255
  for i in range(1, 256):
    # determine off numbered values
    if i % 2 != 0:
      # print each value
      print(i)

print find_odds_in_range()