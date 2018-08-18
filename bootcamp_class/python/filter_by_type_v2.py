# Filter by Type
'''
Write a program that, given some value, tests that value for its type. 
Here's what you should do for each type:
'''
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

# this function will take inputs and based on type and length contents, produce certain results
def filter_by_type(someList):
  current_type = type(someList)

  # this block finds list that comprise integers
  if current_type is int:
    if someList >= 100:
      return "That's a big number!"
      # print "That's a big number!"
    else:
      return "That's a small number"
      # print "That's a small number"

  # this block finds list that comprise strings
  elif current_type is str:
    if len(someList) >= 50:
      return "Long sentence"
    else:
      return "Short sentence"

  elif isinstance(someList, list):
    if len(someList) >= 10:
      return "Big list."
    else:
      return "Short list."


print filter_by_type(sI)
print filter_by_type(mI)
print filter_by_type(bI)
print filter_by_type(eI)
print filter_by_type(sS)
print filter_by_type(mS)
print filter_by_type(bS)
print filter_by_type(eS)
print filter_by_type(aL)
print filter_by_type(lL)
print filter_by_type(eL)
print filter_by_type(spL)