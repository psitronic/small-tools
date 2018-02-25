# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 13:06:28 2018

The implementation of the data staructures:
    LinkedList
Methods:
    add(element)
    delete(element)
    size()
    append(element)
    is_empty()
    search(element)
    
@author: Andrey Sidorenko @psitronic
"""

# to implement a list we need nodes
from node import Node

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
        current_node = self.head
        previous_node = None

        found = False

        while not found and not self.is_empty():

            found = self.search(element)

            if not found:
                previous_node = current_node
                current_node = current_node.get_pointer()
            else:
                if previous_node != None:
                    previous_node.set_pointer(current_node.get_pointer())
                else:
                    self.head = current_node.get_pointer()

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
            