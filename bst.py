#!/usr/bin/env python3

import bt
import sys
import logging

log = logging.getLogger(__name__)

class BST(bt.BT):
    def __init__(self, value=None):
        '''
        Initializes an empty tree if `value` is None, else a root with the
        specified `value` and two empty children.
        '''
        self.set_value(value)
        if not self.is_empty():
            self.cons(BST(), BST())

    def is_member(self, v):
        '''
        Returns true if the value `v` is a member of the tree.
        '''
        #Returns false when bottom has been reached
        if self.is_empty():
            return False
        #Returns true when value has been found in node
        elif self.value() == v:
            return True
        #Returns bool from right when v is larger than node value
        elif v > self.value():
            return self.rc().is_member(v)
        #Returns bool from left v is smaller than node value 
        elif v < self.value():
            return self.lc().is_member(v)
        #Tänk att det är som binary search

    def size(self):
        '''
        Returns the number of nodes in the tree.
        '''
        if self.is_empty():
            return 0
        else:
            return (1 + self.lc().size() + self.rc().size())

    def height(self):
        '''
        Returns the height of the tree.
        '''
        if self.is_empty():
            return 0
        else:
            #Left branch call recursivley
            leftBranch = self.lc().height()
            #Right branch call recursively
            rightBranch = self.rc().height()


            #Returns largets value of rightBranch and leftBranch + 1
            return 1 + max(rightBranch, leftBranch)

    def preorder(self):
        '''
        Returns a list of all members in preorder.
        '''
        if self.is_empty():
            return []
        return [self.value()] + self.lc().preorder() + self.rc().preorder()

    def inorder(self):
        '''
        Returns a list of all members in inorder.
        '''
        if self.is_empty():
            return []
        return self.lc().inorder() + [self.value()] + self.rc().inorder()

    def postorder(self):
        '''
        Returns a list of all members in postorder.
        '''
        if self.is_empty():
            return []
        return self.lc().postorder() + self.rc().postorder() + [self.value()]

    def bfs_order_star(self):
        '''
        Returns a list of all members in breadth-first search* order, which
        means that empty nodes are denoted by "stars" (here the value None).
        '''
        if self.is_empty():
            return []
        queue = []
        size = ((2**self.height())-1)
        returnList = []
        
        queue.append(self)

        while(len(queue)>0):
            returnList.append(queue[0].value()) #Adds value of node in queue
            node = queue.pop(0)

            #Adds left node to queue if not None
            if node.lc() is not None:
                queue.append(node.lc())
            #Adds right node to queue if not None
            if node.rc() is not None:
                queue.append(node.rc())


        #Adds missing nodes, compares temporary and newly added with differing None and '*'
        for i in range (0, size):
            if returnList[i] == None or returnList[i] == '*':
                returnList.insert((i*2)+1, None)
                returnList.insert((i*2)+2, None)

        #Swaps back values from * to None and removes false tail
        for index, value in enumerate(returnList):
            if value is '*':
                returnList[index] = None
            if(len(returnList) > size):
                returnList.pop()


        return returnList

    def add(self, v):
        '''
        Adds the value `v` and returns the new (updated) tree.  If `v` is
        already a member, the same tree is returned without any modification.
        '''
        if self.is_empty():
            self.__init__(value=v)
            return self
        if v < self.value():
            return self.cons(self.lc().add(v), self.rc())
        if v > self.value():
            return self.cons(self.lc(), self.rc().add(v))
        return self

    #Returns node with highest value on left side of self
    def _getMinRight(self):
        if self.lc().value() is not None:
            return self.lc()._getMinRight()
        else:
            return self
    #Returns node with highest value on right side of self
    def _getMaxLeft(self):
        if self.rc().value() is not None:
            return self.rc()._getMaxLeft()
        else:
            return self

    
    def delete(self, v):
        '''
        Removes the value `v` from the tree and returns the new (updated) tree.
        If `v` is a non-member, the same tree is returned without modification.
        '''

        #Searches for node
        if self.is_empty():
            return self
        elif v < self.value():
            return self.cons(self.lc().delete(v), self.rc()) #Tog bort __delete
        elif v > self.value():
            return self.cons(self.lc(), self.rc().delete(v)) #Tog bort __delete
        
        #Remove when node has no children
        if self.lc().value() is None and self.rc().value() is None:
            self.set_value(None)
            self.set_lc(None) #Nulls children so that it works with BFS
            self.set_rc(None) #Nulls children so that it works with BFS
            return self

        #When node has one child
        if self.lc().value() is None:
            temp = self.rc() #Stores child in temp var
            self.set_value(None) #Nulls its value
            return temp #Returns temp
        elif self.rc().value() is None:
            temp = self.lc()
            self.set_value(None)
            return temp

        else:
            #Checks which height is deeper
            righteyHightey = self.rc().height()
            lefteyHightey = self.lc().height()

            #If right child is deeper
            if(righteyHightey > lefteyHightey):
                temp = self.rc()._getMinRight()                   
                self.set_value(temp.value())
                #When minRight has children use cons to swap previous value and conc lc & rc
                if temp.rc().value() is not None:
                    temp.set_value(temp.rc().value())
                    temp.cons(temp.rc().rc(), temp.rc().lc())
                    return self.cons(self.lc(), self.rc()) #Tog bort temp.rc()
                else:
                    self.rc().__delete(temp.value())
                    return self.cons(self.lc(), self.rc())
            #If left child is deeper or equal to right child depth
            else:
                temp = self.lc()._getMaxLeft()          
                self.set_value(temp.value())
                #Maxleft has right children
                if temp.rc().value() is not None:
                    temp.set_value(temp.rc().value())
                    return self.cons(self.lc(), temp.rc())
                #When maxLeft has an inner child (what!?) swap previous value and conc lc and rc
                if temp.lc().value() is not None:
                    temp.set_value(temp.lc().value())
                    temp.cons(temp.lc().lc(), temp.lc().rc())
                    return self.cons(self.lc(), self.rc()) 
                else:
                    self.lc().__delete(temp.value())       
                    return self.cons(self.lc(), self.rc())  


    #Name mangle for delete to stop it from going calling inherited classes with overriding functions
    #__delete = delete #Removed from original code 


if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
