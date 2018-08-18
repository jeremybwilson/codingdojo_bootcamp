# Python program to illustrate
# enumerate function
list1 = ["eat","sleep","repeat"];
s1 = "geek"
 
# creating enumerate objects
obj1 = enumerate(list1)

print "Return type:",type(obj1)
print list(enumerate(list1))

my_list = ["wine","cheese","beer","eat","drink","merry"];
# creating enumerate objects
obj2 = enumerate(my_list)

print "Return type:", type(obj2)
print "The output enumerated is : ", enumerate(obj2)