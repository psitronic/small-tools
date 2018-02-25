# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 13:06:28 2018

The implementation of the data staructures:
    LinkedList
Methods:
    add_element()

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
        Searches for the element in the linked list
        Takes an element
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
        Removes an element from the list
        """
        current_node = self.head
        previous_node = None
        
        found = False
        
        while not found and not self.is_empty():
            
            found = self.search_for(element)

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
        Returns the size of the list
        """
        
        head = self.head # get the first node (head)
        counter = 0

        while head != None:
            counter += 1
            head = head.get_pointer() # move to the next node
            
        return counter
    
    def is_empty(self):
        return self.head == None
        
    def add(self,data):
        new_node = Node(data)
        new_node.set_pointer(self.head)
        self.head = new_node
        
