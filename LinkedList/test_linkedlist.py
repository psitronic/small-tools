# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 09:54:26 2018

The test of the data staructure:
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

@author: andrey
"""

import unittest

from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    
    def setUp(self):
        self.ll = LinkedList()
    
    def test_isEmpty(self):
        self.assertTrue(self.ll.is_empty(), 'The list is not empty')
        self.ll.add(1)
        self.assertFalse(self.ll.is_empty(), 'The list is empty')
        
    def test_print(self):
        self.assertEqual(self.ll.__str__(), '[]')
        self.ll.add(1)
        self.assertEqual(self.ll.__str__(), '[1]')
        self.ll.add(2)
        self.assertEqual(self.ll.__str__(), '[2 -> 1]')

    def test_add(self):
        self.assertIsNone(self.ll.add(1))
        self.assertEqual(self.ll.__str__(), '[1]')
        self.assertIsNone(self.ll.add(2))
        self.assertEqual(self.ll.__str__(), '[2 -> 1]')
        
    def test_insert(self):
        self.assertIsNone(self.ll.insert(0,1))
        self.assertEqual(self.ll.__str__(), '[1]')
        self.assertIsNone(self.ll.insert(1,2))
        self.assertEqual(self.ll.__str__(), '[1 -> 2]')
        self.assertIsNone(self.ll.insert(0,0))
        self.assertEqual(self.ll.__str__(), '[0 -> 1 -> 2]')
        
    def test_index(self):
        self.ll.insert(0,2)
        self.assertEqual(self.ll.index(2), 0)
        self.ll.add(0)
        self.assertEqual(self.ll.index(0), 0)
        
    def test_searh(self):
        self.assertFalse(self.ll.search(2))
        self.ll.add(2)
        self.assertTrue(self.ll.search(2))

    def test_pop(self):
        self.ll.add(1)
        self.ll.add(2)
        self.ll.add(3)
        self.assertEqual(self.ll.pop(),1)
        self.assertEqual(self.ll.pop(),2)
        self.assertEqual(self.ll.pop(),3)
        self.ll.add(1)
        self.ll.add(2)
        self.ll.add(3)
        self.assertEqual(self.ll.pop(0),3)
        self.assertEqual(self.ll.pop(1),1)
        self.assertEqual(self.ll.pop(0),2)
        
    def test_size(self):
        self.assertEqual(self.ll.size(),0)
        self.ll.add(1)
        self.ll.add(2)
        self.ll.add(3)
        self.assertEqual(self.ll.size(),3)
        
    def test_delete(self):
        self.ll.add(1)
        self.ll.add(2)
        self.ll.add(3)
        self.assertIsNone(self.ll.delete(2))
        self.assertEqual(self.ll.__str__(),'[3 -> 1]')        
        self.assertIsNone(self.ll.delete(1))
        self.assertEqual(self.ll.__str__(),'[3]')        
        self.assertIsNone(self.ll.delete(3))
        self.assertEqual(self.ll.__str__(),'[]')  
        
    def test_append(self):
        self.assertIsNone(self.ll.append(1))
        self.assertEqual(self.ll.__str__(),'[1]')  
        self.assertIsNone(self.ll.append(2))
        self.assertEqual(self.ll.__str__(),'[1 -> 2]')  

if __name__ == "__main__":
   unittest.main() 
