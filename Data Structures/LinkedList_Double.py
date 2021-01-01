#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28

@author: emartie7
"""


#Class for a Node to form a doubly linked list
class Node():
    def __init__(self,initVal):
        self.value  = None
        self.next   = None
        self.prev   = None
        if initVal is not None:
            self.value = initVal

class myLinkedList_Double():
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
            NewNode.prev = self.tail
            self.list.append(NewNode)              #New item is the tail
            self.tail.next = NewNode
            self.tail = NewNode                   #update tail
            self.writeIdx += 1
    
    def prepend(self,NewVal):
        if NewVal is not None:
            NewNode         = Node(NewVal)
            NewNode.next    = self.head
            self.list.append(NewNode)        #New item must point to previous head
            self.head.prev = NewNode
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
    
    def PrintListReverse(self):
        CurrItem    = self.tail
        ItemCt      = 0
        while CurrItem is not None:
            print(CurrItem.value)
            CurrItem = CurrItem.prev
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
                NewNode.prev = LeaderRef
                
                self.list.append(NewNode)
                LeaderRef.next = NewNode
                FollowRef.prev = NewNode
                self.writeIdx +=1
                
    def Remove(self,Idx):
        if(Idx == 0):
            self.head       = self.head.next
            self.head.prev  = None
            self.writeIdx -= 1
            
        elif Idx == self.writeIdx:
            TailRef = self.tail.prev
            TailRef.next = None
            self.tail = TailRef
            self.writeIdx -= 1
            
        elif Idx < self.writeIdx:
            RemoveRef = self.traverseToIdx(Idx)
            FollowRef = RemoveRef.next              # Node to be deleted at N
            LeaderRef = RemoveRef.prev
            
            LeaderRef.next = FollowRef
            FollowRef.prev = LeaderRef
                  
            self.writeIdx -= 1
            
        else:
            return print("\nRequested index is out of range\n")
                       
            
testList = myLinkedList_Double(1)
testList.append(2)
testList.append(3)
testList.prepend(4)
testList.append(5)
testList.prepend(6)
testList.Insert(7, 3)
testList.Remove(7)
testList.PrintList()
print("\nList in reverse is: \n")
testList.PrintListReverse()     
