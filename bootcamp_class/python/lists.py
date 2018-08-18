# Manipulating lists

x = [1,2,3,4,5]
x.append(99)
print x
#the output would be => [1,2,3,4,5,99]

x = [99,4,2,5,-3]
print "Output: ", x[:]
#the output would be [99,4,2,5,-3]
print "Output: ", x[1:]
#the output would be [4,2,5,-3];
print "Output: ", x[:4]
#the output would be [99,4,2,5]
print "Output: ", x[2:4]
#the output would be [2,5];

my_list = [1, 'Zen', 'hi']
print len(my_list)  # output => 3

my_list = [1,5,2,8,4]

my_list.append(7)
print "list appended with value of 7 is: ", my_list  # expected output: =>[1,5,2,8,4,7]

# my_list.pop(3)
print "list popped at index value of 3 is: ", my_list.pop(3)
# expected output => [1,5,2,4,7]

my_list = [1,5,2,8,4]
# my_list.index(2)
print "value of list at index[1] is: ", my_list.index(1)
# expected output => index at 1 is 5

my_list.extend(x)
print "my_list extended with list (x) is: ", my_list

# Example 1: Find position of element in the list
# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# element 'e' is searched
index = vowels.index('e')

# index is printed
print('The index of e:', index)

# element 'i' is searched
index = vowels.index('i')

# only the first index of the element is printed
print('The index of i:', index)

# Example 2: Index of element not present in the list
# vowels list
vowels = ['a', 'e', 'i', 'o', 'u']

# element 'p' is searched
# index = vowels.index('p')

# index is printed
print('The index of p:', index)