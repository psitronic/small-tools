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
        
    def is_empty(self):
        return self.head == None
        
    def add_element(self,data):
        new_node = Node(data)
        new_node.set_pointer(self.head)
        self.head = new_node
        
