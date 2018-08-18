# Making Dictionaries
# Create a function that takes in two lists and creates a single dictionary. 
# The first list contains keys and the second list contains the values.
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def making_dictionaries(list1, list2):
  #define new/empty dictionary
  new_dict = {}
  # for the indexes (values) with a range of 0 to the length of list1
  for i in range(0, len(list1)):
    # populate new_dict with values from list 1 as keys, values from list2 as values
    new_dict[list1[i]] = list2[i]
  # return the new dictionary
  return new_dict

# print making_dictionaries(name, favorite_animal)


# my_dict['other_key'] = 'other_value'

my_form = [('name', 'Jeremy'), ('favorite_language', 'Python'), ('hobbies', 'alpine skiing')]
# my_form = [('name', 'Jeremy'), ('name', 'Jeremy'), ('name', 'Jeremy')]

def form_to_dict(form):
  #create an empty dictionary
  result = {}

  # for each set of k/v pairs
  for pair in form:
    # print pair
    # set pair[0] to key
    result[pair[0]] = pair[1]
    # set pair[1] to value

  # return dictionary
  return result

returned_val = form_to_dict(my_form)
print returned_val

# {
#   'name': 'Jeremy',
#   'favorite_language': 'Python',
#   'hobbies': 'alpine skiing'
# }