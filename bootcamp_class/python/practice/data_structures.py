# python really has three primitive data structures

tuple = ('a','b','c')
list = ['a','b','c','x']
dict = {'a':1, 'b': True, 'c': "name"}

list.append('d')  # will add 'd' to the list
list[0]           # will get the first item 'a'

# list.insert(i, x) 
# Insert an item at a given position. The first argument is the index of the element before which to insert, 
# so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.pop(2) # will remove items by position (index), remove the 3rd item
list.remove(x) # Remove the first item from the list whose value is x.

list.index(x) # Return the index in the list of the first item whose value is x. It is an error if there is no such item.

list.count(x) # Return the number of times x appears in the list.

list.sort(cmp=None, key=None, reverse=False) # Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse() # Reverse the elements of the list, in place.