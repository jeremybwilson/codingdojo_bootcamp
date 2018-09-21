def fizz_buzz():
  # specifying a range from 0 to 255
  for num in range(0, 255):
    # dealing with the fact that zero is divisible by any of these numbers
    if num == 0:
      print num
    # if the number in the above range is divisible by either 3 or 5
    elif num % 3 == 0 and num % 5 == 0:
      print 'FizzBuzz'
    # if the number in the above range is divisible by 3
    elif num % 3 == 0:
      print 'Fizz'
    # if the number in the above range is divisible by 5
    elif num % 5 == 0:
      print 'Buzz'
    # elif num % 15 == 0:
      # print 'FizzBuzz'
    else:
      print num

fizz_buzz()