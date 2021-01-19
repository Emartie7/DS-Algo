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
    def __init__(self,initVal=None):
        self.value  = None
        self.next   = None
        self.prev   = None
        if initVal is not None:
            self.value = initVal


#############################################################################
#### class LinkedList_Single_Def
####    Implements a singly linked list utilizinng the "Node" class defined
####    above. Initialization routine allows a single value to be added to
####    the list at the instance of object creation. List is a zero-based index
#############################################################################
class LinkedList_Single_Def():
    def __init__(self,InitVal=None):
        self.list = []
        self.head = Node()
        self.tail = Node()
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
            
        if self.head.value is None:           # If we lose track of head or are initialized w/o one
            self.head = NewNode
            

    def prepend(self,NewVal):
        if NewVal is not None:
            NewNode         = Node(NewVal)
            NewNode.next    = self.head
            self.list.append(NewNode)        #New item must point to previous head
            self.head = NewNode
            self.writeIdx += 1
            
            if self.tail.value is None:           # If we are initialized w/o a value
                self.tail = NewNode

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

    def ReturnList(self,PrintList=0):
        ListValOut  = []
        CurrItem    = self.head
        ItemCt      = 0
        while CurrItem is not None:
            if PrintList == 1:
                print(CurrItem.value)
            ListValOut.append(CurrItem.value)
            CurrItem = CurrItem.next
            if(ItemCt > self.writeIdx):
                break
            else:
                ItemCt += 1
        return ListValOut

    def Insert(self,NewVal,Idx):
        if NewVal is not None:

            if(Idx == 0) or (self.writeIdx == 0):
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
    #############################################################################
    #### def reverse(self)
    ####    Reverses the linked list, making the current head the new tail and
    ####    current tail the new head. This method will traverse the list starting
    ####    at the head. The current node is "N" and this routine will save a reference
    ####    to the next node (N+1), link the current Node "N" to the node at "N-1",
    ####    update the references for current and previous node for the next iteration.
    #############################################################################
    def reverse(self):
        CurrItem = self.head            #Start at the head which will be the new tail
        PrevNode = None
        while CurrItem is not None:
            NextNode = CurrItem.next    #N+1
            CurrItem.next = PrevNode    #Tell CurrItem to point to node at N-1

            PrevNode = CurrItem         #"current" node will be previous node in the next iteration
            CurrItem = NextNode         #"next" node will be the current next in the next iteration
            if CurrItem is None:        #If we are at the "old" tail, this is the new head. While loop will break on next iteration
                self.head = PrevNode

#############################################################################
#### class LinkedList_Double_Def
####    Implements a doubly linked list utilizinng the "Node" class defined
####    above. Initialization routine allows a single value to be added to
####    the list at the instance of object creation.
#############################################################################
class LinkedList_Double_Def():
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
