#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 20:22:33 2021

@author: emartie7
"""

class NodeT:
    def __init__(self,initVal=None):
        self.left = None
        self.right = None
        self.value = initVal

class BinarySearchTree():
    def __init__(self,initVal=None):
        self.root = NodeT(initVal)
        if initVal is not None:
            self.NumLeafs   = 1
            self.levels     = 1
        else:
            self.NumLeafs   = 0
            self.levels     = 1
        
    def insert(self,NewVal):
        # if NewVal > self.root.value:
        #     self.root.right = NodeT(NewVal)
        # else:
        #     self.root.left = NodeT(NewVal)
            
        currNode = self.root
        test = 0
        while currNode is not None:
            if NewVal > currNode.value:
                compareNode = currNode.right        #Get reference to right leaf
                
                if compareNode is None:
                    currNode.right = NodeT(NewVal)  #Update right leaf reference
                    self.NumLeafs += 1
                    self.levels += 1
                    currNode = None
                else:
                    # if NewVal < compareNode.value:
                    #     NewNode = NodeT(NewVal)
                    #     NewNode.right = compareNode
                    #     currNode.right = NewNode
                    # else:
                    currNode = compareNode                   
            else:
                compareNode = currNode.left         #Get reference to left leaf
                
                if compareNode is None:
                    currNode.left = NodeT(NewVal)  #Update left leaf reference
                    self.NumLeafs += 1
                    self.levels += 1
                    currNode = None
                else:                        
                    currNode = compareNode
            
            # if compareNode is None:
            #     compareNode = NodeT(NewVal)
            #     self.NumLeafs += 1
            #     currNode = None
            # else:
            #     currNode = compareNode
            test += 1
            if test > self.NumLeafs:
                currNode = None
                print("Error, entered an infinite loop. Breaking out now. . .")

            
    
myTree = BinarySearchTree(10)
myTree.insert(15)
myTree.insert(5)
myTree.insert(9)
myTree.insert(7)
myTree.insert(11)
print(myTree.root.right.value)