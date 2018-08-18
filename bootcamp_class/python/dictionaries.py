# Dictionaries
# A Dictionary is another mutable set type that can store any number of Python objects, including other set types. 

weekend = {"Sun": "Sunday", "Sat": "Saturday"} #literal notation
capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"

# print "The best day of the weekend is:", weekend["Sun"]
# print "The capital of Slovakia is:", capitals["svk"]

# to print all keys
for data in capitals:
  print "Keys are:", data
# another way to print all keys
for key in capitals.iterkeys():
  print "These are still keys:", key
# to print the values
for val in capitals.itervalues():
  print val
# to print all keys and values
for key,data in capitals.iteritems():
  print key, " = ", data

context = {
  'questions': [
   { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
   { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
   { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
   { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
  ]
 }

def dictionary_key_val_func():
  for key, data in context.items():
    #print data
    for value in data:
      print "Question #", value["id"], ": ", value["content"]
      print "----"

print dictionary_key_val_func()

data ={
  "house":"Haus",
  "cat":"Katze",
  "red":"rot"
}
# print data.items()    #[('house', 'Haus'), ('cat', 'Katze'), ('red', 'rot')]
# print data.keys()     #['house', 'cat', 'red']
# print data.values()   #['Haus', 'Katze', 'rot']

# Dictionaries from Lists
dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]

country_specialities = zip(countries, dishes)
# print "The countries and specialities are:", country_specialities
#Result is...  => [('Italy', 'pizza'), ('Germany', 'sauerkraut'), ('Spain', 'paella'), ('USA', 'hamburger')]

country_specialities_dict = dict(country_specialities)
# print "The countries and specialities are:", country_specialities_dict
#Result is... => {'Germany': 'sauerkraut', 'Spain': 'paella', 'Italy': 'pizza', 'USA': 'hamburger'}

# print "Keys are: ", country_specialities_dict.keys()
# print "Has key value of Spain: ", country_specialities_dict.has_key('Spain')
# print "Values are: ", country_specialities_dict.values()



