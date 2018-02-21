"""
Created on Wed Feb 21 09:46:20 2018

The implementation of the linear data staructures:
    Stack 'Fast In Last Out'
Methods:
    push(element)
    pop()
    peek()
    size()
    is_empty()
    
@author: Andrey Sidorenko @psitronic
"""

class Stack():
    """
    A class to implement the FILO stack sturcture
    """
    def __init__(self):
        
        self.stack = []
        
    def push(self,element):
        """
        Add an element to the bottom of the stack
        """
        
        self.stack.insert(0,element)
        
    def pop(self):
        """
        Pops the bottom element in the stack
        If the stack is not empty removes and returns the bottom element, None otherwise
        """
        try:
            return self.stack.pop(0)
        except IndexError:
            return None

    def peek(self):
        """
        Peeks the bottom element in the stack
        If the stack is not empty returns the bottom element, None otherwise
        """
        try:
            return self.stack[0]
        except IndexError:
            return None
        
    def is_empty(self):
        """
        Check if the satck is empty
        """
        return self.stack == []
    
    def size(self):
        """
        Returns the stack length
        """
        
        return len(self.stack)