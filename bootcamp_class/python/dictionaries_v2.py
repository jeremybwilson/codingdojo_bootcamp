# Making and Reading from Dictionaries
# Create a dictionary containing some information about yourself.

jeremy = {
  "name": "Jeremy",
  "age": 42,
  "city_of_birth": "Bremerton",
  "college": "University of Washington",
  "country": "USA",
  "favorite_language": "Python"
}

def info_about_jeremy(dict):

  for key, value in dict.iteritems():

  # for val in data:

    # print "My name is ", values["first_name"]
    print "My" + " " + key + " " + "is" + " " + str(value)
    print "----"
    # print "My age is ", val["age"]
    # print "----"
    # print "My country of birth is ", val["country"]
    # print "----"
    # print "My favorite language is ", val["favorite_language"]
    # print "----"

info_about_jeremy(jeremy)