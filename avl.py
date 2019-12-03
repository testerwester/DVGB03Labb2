#!/usr/bin/env python3

import sys
import bst
import logging

log = logging.getLogger(__name__)

class AVL(bst.BST):
    def __init__(self, value=None):
        '''
        Initializes an empty tree if `value` is None, else a root with the
        specified `value` and two empty children.
        '''
        self.set_value(value)
        if not self.is_empty():
            self.cons(AVL(), AVL())

    def add(self, v):
        '''
        Example which shows how to override and call parent methods.  You
        may remove this function and overide something else if you'd like.
        '''
        return bst.BST.add(self, v).balance()

    def delete(self, v):
        '''
        Deletes values by calling delete function from BST, balances tree and returns value.
        '''
        print("Running delete")
        return bst.BST.delete(self, v).balance()

    def balance(self):
        '''
        AVL-balances around the node rooted at `self`.  In other words, this
        method applies one of the following if necessary: slr, srr, dlr, drr.
        '''
        #Checks either side of self for balance and existance
        if self.lc() is not None:
            leftHeight = bst.BST.height(self.lc())
        else: 
            leftHeight = 0

        if self.rc() is not None:
            rightHeight = bst.BST.height(self.rc())
        else: 
            rightHeight = 0

        #Gets absolute sum of left and right height
        difference = abs(leftHeight - rightHeight)

        #Unbalanced
        if difference >= 2:
            print("Unbalanced")
            #Case 1 eller 2
            if self.lc().height() >= self.rc().height():
                #Case 1 SRR
                if self.lc().lc().height() >= self.lc().rc().height():
                    print("SRR")
                    return self.srr()
                else: # self.lc().lc().height() < self.lc().rc().height():
                    print("DRR")
                    return self.drr()
                #else:
                    #return self.cons(self.lc().balance(), self.rc())
            #Case 3 or 4        
            else:
                #Case 3 DLR
                if self.rc().lc().height() > self.rc().rc().height():
                    print("DLR")
                    return self.dlr()
                else: # self.rc().lc().height() < self.rc().rc().height():
                    print("SLR")
                    return self.slr()
                #else:
                    #return self.cons(self.lc(), self.rc().balance())
        else:
            return self

    #Rotate left
    def slr(self):
        '''
        Performs a single-left rotate around the node rooted at `self`.
        '''
        n1 = self.rc()
        self.set_rc(n1.lc())
        n1.set_lc(self)
        return n1

    #Rotate right
    def srr(self):
        '''
        Performs a single-right rotate around the node rooted at `self`.
        '''
        n1 = self.lc()
        self.set_lc(n1.rc())
        n1.set_rc(self)
        return n1

    #Rotate double right left
    def dlr(self):
        '''
        Performs a double-left rotate around the node rooted at `self`.
        '''
        self.set_rc(self.rc().srr())
        return self.slr()

    #Rotate double left right
    def drr(self):
        '''
        Performs a double-right rotate around the node rooted at `self`.
        '''
        self.set_lc(self.lc().slr())
        return self.srr()

if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
