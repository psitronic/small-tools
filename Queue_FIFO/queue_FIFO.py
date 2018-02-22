"""
Created on Wed Feb 21 09:46:20 2018

The implementation of the linear data staructures:
    Queue 'Fast In First Out'
Methods:
    add(element)
    get()
    size()
    is_empty()

@author: Andrey Sidorenko @psitronic
"""


class Queue():
    """
    A class to implement the FIFO queue sturcture
    """
    def __init__(self):

        self.queue = []

    def add(self, element):
        """
        Adds an element to the rear end of the queue
        """

        self.queue.insert(0, element)

    def get(self):
        """
        Gets the front element in the queue
        If the queue is not empty removes and returns
        the front element, None otherwise
        """
        try:
            return self.queue.pop()
        except IndexError:
            return None


    def is_empty(self):
        """
        Checks if the queue is empty
        """
        return self.queue == []

    def size(self):
        """
        Returns the queue length
        """

        return len(self.queue)
