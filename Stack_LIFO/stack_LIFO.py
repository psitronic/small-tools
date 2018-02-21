"""
Created on Wed Feb 21 09:46:20 2018

The implementation of the linear data staructures:
    Stack 'Last In First Out'
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
    A class to implement the LIFO stack sturcture
    """
    def __init__(self):
        
        self.stack = []
        
    def push(self,element):
        """
        Add an element to the top of the stack
        """
        
        self.stack.append(element)
        
    def pop(self):
        """
        Pops the top element in the stack
        If the stack is not empty removes and returns the top element, None otherwise
        """
        try:
            return self.stack.pop()
        except IndexError:
            return None

    def peek(self):
        """
        Peeks the top element in the stack
        If the stack is not empty returns the top element, None otherwise
        """
        try:
            return self.stack[len(self.stack) - 1]
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