# Python program to illustrate
# functions

jeremy = {
  "first_name": "Jeremy",
  "last_name": "Wilson"
}
alex = {
  "first_name": "Alex",
  "last_name": "Wilson"
}

def printDictionary(times):  # times is the parameter the function will be fed
  # for key in jeremy:
  for i in range(0, times):
    for key in jeremy:
      print jeremy[key]

printDictionary(2)
