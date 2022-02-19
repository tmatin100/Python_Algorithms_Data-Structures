# Iterative Binary Search Example

def binary_search(list, target): 
	first = 0                         # points to the first element in the list
	last = len(list) - 1              # points to the last element in the list

	while first <= last: 
		midpoint = (first + last)//2     # This is how we calcualte a midpoint
		if list[midpoint] == target:     # if the value of the midpoint is the same as the target, 
	  		return midpoint              
		elif list[midpoint] < target:     # if the value of the midpoint is less than the target
			first = midpoint + 1           # we discard everyhing thats lower than the midpoint, and redifine the starting point by setting the to the value of first after the midpoint which is midpoint +1
		else: 
	   		last = midpoint - 1          # if the value is greater than the midpoint, then we discard the values after the midpoint, and redifne last to point to the value prior to midpoint, which is midpoint - 1
	return None 

numbers = [1,2,3,4,5,6,7,8,9,10]  #the list has to be sorted 

def varify(index): 
	if index is not None: 
		print("Target found at index:", index)
	else: 
		print("Target not found in list")

result = binary_search(numbers, 12)
varify(result)

result = binary_search(numbers, 6)
varify(result)


