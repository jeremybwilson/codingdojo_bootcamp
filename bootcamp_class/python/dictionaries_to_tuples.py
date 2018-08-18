# Dictionary in, tuples out
# Write a function that takes in a dictionary and returns a list of tuples where the first tuple item is the key and the second is the value.

# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#function output => [("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]

def dict_to_tuples(my_dict):

  # define an empty list 
  new_list = []
  # here, k and v will parse each tuple of key,value pairs returned by .iteritems()
  for key, value in my_dict.iteritems():
    # push (or append) the values to the new tuple
    new_list.append((key, value))
  # return the value
  return new_list

print dict_to_tuples(my_dict)