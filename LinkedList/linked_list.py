# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 13:06:28 2018

The implementation of the data staructures:
    LinkedList
Methods:
    add(element)
    append(element)
    delete(element)    
    index(element)
    insert(index, element)
    is_empty()
    pop()
    pop(index)
    search(element)
    size()
    __str__()
    
@author: Andrey Sidorenko @psitronic
"""

# to implement a list we need nodes
#from node import Node

class Node(object):
    """
    A class to implement a node
    """
    def __init__(self,value = None):
        
        self.value = value
        self.pointer = None
        
    def get_value(self):
        """
        Returns the value of the node
        """
        return self.value
    
    def get_pointer(self):
        """
        Returns the reference to the next node
        """
        return self.pointer
    
    def set_pointer(self,pointer):
        """
        Sets the reference to the next node
        """
        self.pointer = pointer


class LinkedList(object):
    """
    A class to implement the linked list
    """
    def __init__(self):

        self.head = None

    def search(self, element):
        """
        Searches for the element in the linked list.
        Takes an element.
        Returns True if the element in the list, False otherwise
        """
        node = self.head # get the first node (head)

        while node != None:            
            if element == node.get_value():
                return True
            node = node.get_pointer() # move to the next node

        return False

    def delete(self, element):
        """
        Removes an element from the list.
        Takes an element to remove.
        Modifies the list.
        Returns nothing.
        """
        current = self.head
        previous = None

        while current != None and not self.is_empty():

            if element == current.get_value():
                if previous != None:
                    previous.set_pointer(current.get_pointer())
                else:
                    self.head = current.get_pointer()
                break
            else:
                previous = current
                current = current.get_pointer()
                

    def size(self):
        """
        Returns the number of elements in the list
        """
        head = self.head # get the first node (head)
        counter = 0

        while head != None:
            counter += 1
            head = head.get_pointer() # move to the next node

        return counter

    def is_empty(self):
        return self.head == None

    def add(self, data):
        """
        Adds a new element to the list
        Takes an element
        Returns nothing
        """
        new_node = Node(data)
        new_node.set_pointer(self.head)
        self.head = new_node

    def append(self, element):
        """
        Adds a new element to the end of the list making it the last element
        in the list
        Takes an element
        Returns nothing
        """
        current = self.head # get the first node (head)
        previous = None
        # searching for the last element in the list
        # the last element has a pointer to None
        if self.is_empty():
            self.add(element)
        else:
            while current != None:
                previous = current            
                current = current.get_pointer() # move to the next node
    
            new_node = Node(element) # create a new node with data and pointer to None
            new_node.set_pointer(None)
            previous.set_pointer(new_node) # set the pointer of previous last to the new las node

    def index(self, element):
        """
        Returns the position of element in the list.
        Takes an element.
        Returns an index.
        """
        node = self.head # get the first node (head)
        counter = 0

        while node.get_value() != element: # do it unless the element found
            counter += 1 # count the position number
            node = node.get_pointer() # move to the next node
    
        return counter
        
    def insert(self, index, element):
        """
        Adds a new element to the list at position index
        """
        if index == 0:
            self.add(element) # add the element to the front end
        elif index == self.size() + 1:
            self.append(element)  # add the element to the rear end
        elif index > 0 and index < self.size() + 1:
            counter = 1
            current = self.head # get the first node (head)
            previous = None
            while counter != index + 1:
                counter += 1
                previous = current # remember the current node
                current = current.get_pointer() # move to the next node
                
            new_node = Node(element) # create a new node
            new_node.set_pointer(current) # link the new node to the next
            previous.set_pointer(new_node) # link the previous node to the new
        else:
            raise Exception("IndexError: list index out of range")
            
    def pop(self, index = None):
        """
        Removes and returns the element at the index postion in the list.
        Returns the removed element
        """        
        current = self.head # get the first node (head)
        previous = None
        counter = 0
        # if no index provided then pop the last element in the list
        if index == None:
            while counter < self.size() - 1:
                counter += 1
                previous = current # remember the current node
                current = current.get_pointer() # move to the next node
            
            if previous != None:
                previous.set_pointer(None)
            else:
                self.head = current.get_pointer()
        else: # else pop the element at the position index
            while counter < self.size():
                if counter == index:
                    if previous != None:
                        previous.set_pointer(current.get_pointer())
                    else:
                        self.head = current.get_pointer()
                    break
                else:
                    counter += 1
                    previous = current
                    current = current.get_pointer()

        return current.get_value()
    
    def __str__(self):
        """
        Returns a string representation of the list
        """
        current = self.head # get the first node (head)
        result = ''
        
        while current != None:
            result = result + str(current.get_value()) + " -> "
            current = current.get_pointer() # move to the next node
        result = result[:-4]

        return '[{}]'.format(result)

