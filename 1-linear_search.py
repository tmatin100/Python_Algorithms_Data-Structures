# Linear Search Example

#Algorithm Gideline
"""
The steps in the algorithm need to be in a very specific order. 
The steps also need to be distinct
The algorith m should produce a resut
The algorithm should complete in a finite ammount of time 
"""

def linear_search(list, target):
    """ Returns the index position of the traget if found, else returns None
    """
    for i in range(0,len(list)):
      if list[i] == target: 
        return i 
    return None 

""" The code can be cleaned up a bit by using the enumerate function on the list.
def linear_search(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1    
"""
 
numbers = [1,2,3,4,5,6,7,8,9,10]

def varify(index): 
  if index is not None: 
    print("Target found at index:", index)
  else: 
    print("Target not found in list")

result = linear_search(numbers, 12)

varify(result)





