#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 20:22:33 2021

@author: emartie7
"""

class NodeT:
    def __init__(self,initVal=None):
        self.parent = None
        self.left   = None
        self.right  = None
        self.value  = initVal

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
        currNode = self.root
        test = 0
        while currNode is not None:
            if NewVal > currNode.value:
                compareNode = currNode.right        #Get reference to right leaf
                
                if compareNode is None:
                    NewNode = NodeT(NewVal)
                    NewNode.parent = currNode
                    currNode.right = NewNode  #Update right leaf reference
                    self.NumLeafs += 1
                    self.levels += 1
                    currNode = None
                else:
                    currNode = compareNode                   
            else:
                compareNode = currNode.left         #Get reference to left leaf
                
                if compareNode is None:
                    NewNode = NodeT(NewVal)
                    NewNode.parent = currNode
                    currNode.left = NewNode
                    self.NumLeafs += 1
                    self.levels += 1
                    currNode = None
                else:                        
                    currNode = compareNode

            test += 1
            if test > self.NumLeafs:
                currNode = None
                print("Error, entered an infinite loop. Breaking out now. . .")
                
    def lookup(self,LookupVal):
        CurrNode = self.root
        NextNode = self.root
        test = 0
        while(CurrNode is not None):
            print("Current Node value is: {}".format(CurrNode.value))
            if(CurrNode.value == LookupVal):
                print("Found node with value: {}".format(LookupVal))
                return CurrNode
                # NextNode = None
            else:
                if(LookupVal>CurrNode.value):
                    #go right
                    NextNode = CurrNode.right
                else:
                    NextNode = CurrNode.left
            CurrNode = NextNode
                
            test += 1
            if test > self.NumLeafs:
                CurrNode = None
                print("Error, entered an infinite loop or value not found. Breaking out now. . .")
        if NextNode is None:
            print("Warning: Value {} not found.".format(LookupVal))
        return CurrNode
    
    def remove(self,RemoveValue):
        RemoveNode = self.lookup(RemoveValue)
        if RemoveNode is not None:
            #Remove if node was found
            ParentRef = RemoveNode.parent
            if RemoveNode.right is not None:                #Remove node to be replaced by left branch
                if RemoveNode == ParentRef.left:            #Removed value < Parent value
                    #Update parent left branch pointers
                    ParentRef.left = RemoveNode.right
                    RemoveNode.parent = None
                    UpdateNode = ParentRef.left             #UpdateNode is the non-null Node that now holds the "place" of the removed node
                else:                                       #Removed Value > Parent value
                    #Update parent right branch pointers
                    ParentRef.right = RemoveNode.right
                    RemoveNode.parent = None
                    UpdateNode = ParentRef.right
                if RemoveNode.left is not None:             #Update Right node parent if it exists (left and right node exist)
                    UpdateNode.left = RemoveNode.left
                    RemoveNode.left.parent = UpdateNode

            elif(RemoveNode.left is not None):             #Remove Node to be replaced by right branch
                if RemoveNode == ParentRef.left:
                    #Update parent left branch pointers
                    ParentRef.left = RemoveNode.left    #Update parent left branch pointers
                    RemoveNode.parent = None
                else:
                    #Update parent right branch pointers
                    ParentRef.right = RemoveNode.left
                    RemoveNode.parent = None
            else:
                #No children on remove node
                if RemoveNode == ParentRef.left:
                    ParentRef.left = None
                else:
                    ParentRef.right = None
        else:
            return None



myTree = BinarySearchTree(9)
myTree.insert(4)
myTree.insert(20)
myTree.insert(1)
myTree.insert(6)
myTree.insert(15)
myTree.insert(170)
myTree.lookup(15)
myTree.lookup(6)
myTree.remove(4)
RetrievedNode = myTree.lookup(1)
print("Found node with value: {}, left child: {}, right child: {}, and parent {}".format(RetrievedNode.value,RetrievedNode.left,RetrievedNode.right,RetrievedNode.parent.value))
