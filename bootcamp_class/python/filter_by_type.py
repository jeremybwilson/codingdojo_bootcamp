sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

# Integer
# If the integer is greater than or equal to 100, print "That's a big number!" 
# If the integer is less than 100, print "That's a small number"

# String
# If the string is greater than or equal to 50 characters print "Long sentence." 
# If the string is shorter than 50 characters print "Short sentence."

# List
# If the length of the list is greater than or equal to 10 print "Big list!" 
# If the list has fewer than 10 values print "Short list."

def filter_for_integer(value):

  current_tester = value
  current_type = type(current_tester)

  # define if value is integer
  if current_type is int:

    # check if number is >= 100
    if current_tester >= 100:
      print "That's a big number!"

    # check if number is < 100
    elif current_tester < 100:
      print "That's a small number!"

  # define if value is string
  elif current_type is str:

    # determine string is longer than 50
    if len(current_tester) >= 50:
      print "That is a long sentence."
    # print short sentence message
    else:
      print "That is a short sentence."

  # define if value is list
  elif isinstance(current_tester, list):
    # determine if value is a list
    if len(current_tester) >= 10:
      print "Big list!"
    # print short list message
    else:
      print "Short list!"

filter_for_integer(sI)
filter_for_integer(mI)
filter_for_integer(bI)
filter_for_integer(eI)
filter_for_integer(spI)
filter_for_integer(sS)
filter_for_integer(mS)
filter_for_integer(bS)
filter_for_integer(eS)
filter_for_integer(aL)
filter_for_integer(mL)
filter_for_integer(lL)
filter_for_integer(eL)
filter_for_integer(spL)
