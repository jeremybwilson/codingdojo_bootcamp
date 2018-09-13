# Assignment: User
class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = False

    def login(self):
        self.logged = True
        print (self.name + " is logged in.")
        return self

    def logout(self):
        self.logged = False
        print (self.name + " is now logged out.")
        return self
        
    def show(self):
        print ("My name is {}. You can email me at {}".format(self.name, self.email))
        return self

user1 = User("Jeremy", "jeremybwilson@gmail.com")
user2 = User("Alex", "alexg15@gmail.com")
user3 = User("Anika", "jeremybwilson@gmail.com")

user1.login().show().logout()
print ("\n")
user2.login().show()
print ("\n")
user3.login().show().logout()
print ("\n")