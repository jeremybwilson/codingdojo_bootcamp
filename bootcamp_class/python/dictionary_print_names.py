# Names
# Given the following dictionaries, write out the names as follows:
# output => Jeremy Wilson

students = [
  {'first_name':  'Michael', 'last_name' : 'Jordan'},
  {'first_name' : 'John', 'last_name' : 'Rosales'},
  {'first_name' : 'Mark', 'last_name' : 'Guillen'},
  {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

# define the function
def show_all_students(list):

  for student in students:

    print student["first_name"] + " " + student["last_name"]

show_all_students(students)

users = {
  'Students': [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
  'Instructors': [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
}

# define a function to show all users
def show_all_users(users):

  for role in users:
    counter = 0
    print role
    for person in users[role]:
      counter += 1
      # print counter
      first_name = person["first_name"].upper()
      last_name = person["last_name"].upper()
      length = len(first_name) + len(last_name)
      # print out info in requested format => COUNT - FIRSTNAME LASTNAME - LENGTH
      print counter, "-", first_name, last_name, "-", length


print show_all_users(users)