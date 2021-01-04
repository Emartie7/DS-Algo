#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 19:41:14 2020

@author: emartie7
"""

#############################################################################
#### class Node
####    Defined a "node" object that contains a value and a a singled "link" 
####    or reference to another object. Intialization routine allows for  
####    setting a value. Links must be defined externally.
#############################################################################
class Node():
    def __init__(self,initVal):
        self.value  = None
        self.next   = None
        if initVal is not None:
            self.value = initVal
            
            
#############################################################################
#### class LinkedList_Single_Def
####    Implements a singly linked list utilizinng the "Node" class defined
####    above. Initialization routine allows a single value to be added to
####    the list at the instance of object creation.
#############################################################################
class LinkedList_Single_Def():
    def __init__(self,InitVal):
        self.list = []
        self.head = Node
        self.tail = Node
        self.writeIdx = 0
        
        if InitVal is not None:
            NewNode = Node(InitVal)
            self.list.append(NewNode)
            self.head = NewNode
            self.tail = NewNode
            self.writeIdx = 1
            
    def append(self,NewVal):
        if NewVal is not None:   
            NewNode = Node(NewVal)
            self.list.append(NewNode)              #New item is the tail
            self.tail.next = NewNode
            self.tail = NewNode                   #update tail
            self.writeIdx += 1
    
    def prepend(self,NewVal):
        if NewVal is not None:
            NewNode         = Node(NewVal)
            NewNode.next    = self.head
            self.list.append(NewNode)        #New item must point to previous head
            self.head = NewNode
            self.writeIdx += 1

    def traverseToIdx(self,Idx):
        if Idx is not None:
            CurrItem = self.head
            NodeIdx = 0
            while CurrItem is not None:
                if(NodeIdx == Idx):
                    return CurrItem
                else:
                    NodeIdx += 1
                    CurrItem = CurrItem.next
    
    def PrintList(self):
        CurrItem    = self.head
        ItemCt      = 0
        while CurrItem is not None:
            print(CurrItem.value)
            CurrItem = CurrItem.next
            if(ItemCt > self.writeIdx):
                break
            else:
                ItemCt += 1
              
    def Insert(self,NewVal,Idx):
        if NewVal is not None:
            
            if(Idx == 0):
                self.prepend(NewVal)
            elif Idx >= self.writeIdx:
                self.append(NewVal)
            else:
                NewNode = Node(NewVal)                  #Node to be inserted at position N
                LeaderRef = self.traverseToIdx(Idx-1)   #Node at position N-1
                FollowRef = LeaderRef.next              #Node currently at position N
                
                NewNode.next = FollowRef
                self.list.append(NewNode)
                LeaderRef.next = NewNode
                self.writeIdx +=1
                
    def remove(self,Idx):
        if(Idx == 0):
            self.head = self.head.next
            self.writeIdx -= 1
        elif Idx < self.writeIdx:
            LeaderRef = self.traverseToIdx(Idx-1)   # Node at N-1
            RemoveRef = LeaderRef.next              # Node to be deleted at N
            
            LeaderRef.next = RemoveRef.next  #Tell leader to point to node at N+1
            self.writeIdx -= 1
            if RemoveRef.next is None:
                self.tail = LeaderRef
        else:
            return print("\nRequested index is out of range\n")
            
            
            
                
            
            
            
# testList = LinkedList_Single_Def(1)
# testList.append(2)
# testList.append(3)
# testList.prepend(4)
# testList.append(5)
# testList.prepend(6)
# testList.PrintList()
# testList.Insert(7, 3)
# print("\n")
# testList.PrintList()
# testList.remove(15)
# print("\n")
# testList.PrintList()          
