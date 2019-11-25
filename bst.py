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
        logging.info("TODO@src/bst.py: implement is_member()")
        return False
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

        For example, consider the following tree `t`:
                    10
              5          15
           *     *     *     20

        The output of t.bfs_order_star() should be:
        [ 10, 5, 15, None, None, None, 20 ]
        '''

        if self.is_empty():
            return []
        
        queue = []
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

        #Removes unescessary None at line that shouldn't be showed
        for x in reversed(returnList):
            if x == None:
                returnList.pop()
            else:
                break


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
    
    def delete(self, v):
        '''
        Removes the value `v` from the tree and returns the new (updated) tree.
        If `v` is a non-member, the same tree is returned without modification.
        '''
        log.info("TODO@src/bst.py: implement delete()")
        return self

if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
