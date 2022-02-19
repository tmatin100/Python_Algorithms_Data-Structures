# The Array data structure, in python is called a list 
#Arrays are particullary good at accessing and reading data, which happens in constant time. However, 
#arrays are pretty bad at inserting and deleting both which happens in linear time. For that reason, 
#using a data structre called Linked list is a better option. 

new_list = [1,2,3]
result = new_list[0]
print(result)

# When we search for an item in a list, even though accessing in consant time, having to do this for every element eventualy results in linear time. 

#let's look at how search works 
if 1 in new_list: print (True)

# we can use a for lo0p to itterate over the list (liniear search)

for n in new_list: 
    if n==1: 
        print(True)
    break 

#insert operation, has an linear runtime
#appending , insterts at the end of a list
#nubmers currently has one elemnt
numbers = []
print(len(numbers)

#lets see what happens when we append an item to the end of this new_list
numbers = []
numbers.append(2)
print(len(numbers)

#the list permorms a list resize allocation operation when we append an element to it, in this manner 0,4,8,16,25,35,46 . 
#because of this append operations have an ammortized constant time 
# extend takes the elements and adds it to the list 
numbers = []
numbers.extend([4,5,6,])
numbers

#delete operations shifts every element to the left, has a O(n)-Linear Runtime

