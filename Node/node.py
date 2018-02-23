# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 12:28:55 2018

The implementation of the linear data staructures:
    Node
Methods:
    get_value()
    get_pointer()
    set_pointer()

@author: Andrey Sidorenko @psitronic
"""


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
