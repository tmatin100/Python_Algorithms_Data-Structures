# Recursive Binary Search Example
"""
A recursive function is a fucntion that calls itself.
The way we've tackled the recursive version of binary serach is by using a combination
of a recursive call and the iterative approach with start and end variables to keep track
of the portion of the list we're searching.
"""

def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint=(len(list))//2
        if list[midpoint] == target: 
            return True
        else: 
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else: 
                return recursive_binary_search(list[:midpoint], target)

def varify(result):
    print("Target found: ", result)


numbers = [1,2,3,4,5,6,7,8]

result = recursive_binary_search(numbers, 12)
varify(result)

result = recursive_binary_search(numbers, 6)
varify(result)
