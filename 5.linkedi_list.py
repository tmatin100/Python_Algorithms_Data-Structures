# Linkedi List 
# A linked list is a linear data structure, where each element in the list is contained in a seperate object called a node.
# A node models two pieces of information, an individual item of the data we want to store, and a reference to the next noede in the list. 
# The first node in the list is called the head of the list, and the last node is called a tail. The head and the tail nodes are special.
# The list only maintains a reference to the head, and some implementations keeps reference to the tail as well( double linked list).
# Every node other than the tail points to the next node in the list, but the tail doesn't point to anytinhg, it denotes the end of the list. 
#Nodes are whats called self-referntial objects
#If we are dealing with a problem which involves a lot of inserting and deletion of items, a linked list is a better option. 


class Node: 
    """
    An object for storing a single node of a linkedin list. 
    Models two attributes - data and the link to the next node in the list. 
    """
    data = None
    next_node = None 

    def __init__(self, data):
        self.data = data

    def __repr__(self, data):
        #string represention of what we want to be printed in the console, %s is a way to substitue something into a string,  aka string interpolation. 
        return "<Node data: %s>" % self.data  #we want to replace %s with self.data 

#lets create a class that defines a head of a linkedin list
class LinkedList: 
"""Singley linked list"""
    def __init__(self):
        self.head = None 
    def is_empty(self):
        return self.head == None

# convinence method, makes existing method easier to use 
   def size(self):
       """
       Returns the number of nodes in the list 
       Takes 0(n) time
       """
       current = self.head
       count = 0 

       while current: 
           count += 1
           current = current.next_node
        return count

    def add(self, data):
        """Adds a new Node containing data at the head of the list
        Takes constant time 0(1), which is our best case scenario.
        """
        new_node=Node(data)
        new_node.next_node =self.head
        self.head=new_node




