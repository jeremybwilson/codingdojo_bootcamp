ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []

fruits = ["apple","banana","orange","strawberry"]
vegetables = ["lettuce","cucumber","carrots"]

fruits_and_vegetables = fruits + vegetables
print fruits_and_vegetables
salad = 3 * vegetables
print salad

drawer = ['documents', 'envelopes', 'pens']
#access the drawer with index of 0 and print value
# print drawer[0]  #prints documents
#access the drawer with index of 1 and print value
# print drawer[1] #prints envelopes
#access the drawer with index of 2 and print value
# print drawer[2] #prints pens

x = [99,4,2,5,-3];
#print x[:]
#the output would be [99,4,2,5,-3]
#print x[1:]
#the output would be [4,2,5,-3];
# print x[:4]
#the output would be [99,4,2,5]
# print x[2:4]
#the output would be [2,5];

my_list = [1, 'Zen', 'hi'];
# print len(my_list)
# output => 3

my_list2 = [1,5,2,8,4];
my_list3 = [10,20,30];
new_value = 7
print my_list2.append(my_list3)

print "Appending value of 7 to my_list : ", my_list2.append(new_value)
print "The minimum of my_list is : ", min(my_list2)
print "The output sorted is : ", sorted(my_list2)

# print my_list
# output: => [1,5,2,8,4,7]

my_list4 = [1,5,2,8,4,7];
my_list5 = [10,15,20,25,30];

print "Extended list : ", my_list4.extend(my_list5)

print "The list popped is : ", my_list4.pop(4) # pops the 4th index out to a separate variable

index_val = 1
print my_list.index(index_val)