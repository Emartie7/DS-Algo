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
            # print("Current Node value is: {}".format(CurrNode.value))
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
    
    def findMinimum(self,subRoot):
        CurrNode = subRoot
        NextNode = subRoot.left
        while(NextNode is not None):
            CurrNode = NextNode
            NextNode = CurrNode.left
        print("Minimum tree value is: {}".format(CurrNode.value))
        return CurrNode
    
    def remove(self,RemoveValue):
        RemoveNode = self.lookup(RemoveValue)
        if RemoveNode is not None:
            #Remove if node was found
            ParentRef = RemoveNode.parent
            if ((RemoveNode.left is None) and (RemoveNode.right is None)):              #No children
                if RemoveNode == ParentRef.left:
                    ParentRef.left = None
                else:
                    ParentRef.right = None
            elif((RemoveNode.left is not None) and (RemoveNode.right is not None)):     #Two Children
                MinNode = self.findMinimum(RemoveNode)
                if RemoveNode == ParentRef.left:
                    ParentRef.left = MinNode        #Minimum value takes the place of the removed value
                else:
                    ParentRef.right = MinNode
                MinNode.left = RemoveNode.left
                MinNode.right = RemoveNode.right
                MinParent = MinNode.parent      #Get a reference to the parent of the minimum value
                MinNode.parent = ParentRef      #Update the parent of the minimum node (now in the place of the removed node)
                MinParent.left = None           #Former parent of minimum value loses its left  child 
            else:
                if RemoveNode.left is not None:             #Removed node has left child
                    if RemoveNode == ParentRef.left:
                        ParentRef.left = RemoveNode.left
                    else:
                        ParentRef.right = RemoveNode.left
                else:                                       #Removed node has right child
                    if RemoveNode == ParentRef.left:
                        ParentRef.left = RemoveNode.right 
                    else:
                        ParentRef.right = RemoveNode.right
            return RemoveNode              
        else:
            return None



myTree = BinarySearchTree(9)
myTree.insert(4)
myTree.insert(20)
myTree.insert(1)
myTree.insert(6)
myTree.insert(15)
myTree.insert(170)
myTree.insert(13)
myTree.insert(19)
myTree.remove(20)
# myTree.findMinimum(myTree.root)
# print("Found node with value: {}, left child: {}, right child: {}, and parent {}".format(RetrievedNode.value,RetrievedNode.left,RetrievedNode.right,RetrievedNode.parent.value))
