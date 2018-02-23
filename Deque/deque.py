"""
Created on Wed Feb 23 11:51:20 2018

The implementation of the linear data staructures:
    Deque
Methods:
    add(element)
    get()
    size()
    is_empty()

@author: Andrey Sidorenko @psitronic
"""


class Deque():
    """
    A class to implement the deque sturcture
    """
    def __init__(self):

        self.deque = []

    def add_rear(self, element):
        """
        Adds an element to the rear end of the deque
        """

        self.deque.insert(0, element)

    def add_front(self, element):
        """
        Adds an element to the front end of the deque
        """

        self.deque.append(element)

    def get_front(self):
        """
        Gets the front element in the deque
        If the deque is not empty removes and returns
        the front element, None otherwise
        """
        try:
            return self.deque.pop()
        except IndexError:
            return None

    def get_rear(self):
        """
        Gets the rear element in the deque
        If the deque is not empty removes and returns
        the rear element, None otherwise
        """
        try:
            return self.deque.pop(0)
        except IndexError:
            return None

    def is_empty(self):
        """
        Checks if the deque is empty
        """
        return self.deque == []

    def size(self):
        """
        Returns the deque length
        """

        return len(self.deque)
