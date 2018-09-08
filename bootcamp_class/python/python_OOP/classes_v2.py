class Person(object):
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def introduce(self):
        print ("Hello, my name is {}".format(self.name))

    def display(self):
        print (self.__dict__)

class Ninja(Person):
    def __init__(self, ninja_name, ninja_age, ninja_height):
        super(Ninja, self).__init__(ninja_name, ninja_age, ninja_height)
        self.stealth = 100
        self.attack_skill = 30
        self.defense_skill = 10

    def attack(self):
        print ("Attacking!!!")
        self.health -= 10

class Coder(Person):
    def __init__(self, coder_name, coder_age, coder_height):
        super(Coder, self).__init__(coder_name, coder_age, coder_height)
        self.favorite_language = "Python"

person1 = Person("Jeremy", 43, 70)
person2 = Person("Alex", 17, 70)
ninja1 = Ninja("Bruce Lee", 44, 72)
coder1 = Coder("Patrick", 200000, 9999)

coder1.display()
# ninja1.introduce()
# print (ninja1.__dict__)
# ninja1.attack()
# ninja1.display()
# print (ninja1.health)
# ninja1.display()
# print (ninja1)
# print (person1.__dict__)
# print (person1.name)
# print (person2.name)
# person1.display()
# person2.display()