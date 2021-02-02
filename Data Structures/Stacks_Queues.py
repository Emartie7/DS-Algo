#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 18:05:05 2021

@author: emartie7
"""

import LinkedLists

MAX_STACK_LEN = 128

class Stack():
    def __init__(self,InitVal=None):
        self.NodeList = LinkedLists.LinkedList_Single_Def()
        # for x in range(0,MAX_STACK_LEN-1):
        #     self.NodeList.append(x)
        
        self.top = None
        self.bottom = None
        self.length = 0
        
        if InitVal is not None:
            self.NodeList.append(InitVal)
            self.bottom     = self.NodeList.head
            self.top        = self.NodeList.tail
            self.length     += 1
            
    def peek(self):
        return self.top.value
    
    def push(self,Val):
        if (self.length < MAX_STACK_LEN):
            self.NodeList.append(Val)
            self.top = self.NodeList.tail
            self.length +=1
        else:
            print("\nMax stack size reached, additional elements will not be added")

    def pop(self):
        if(self.length > 0):
            Popped = self.NodeList.tail
            self.NodeList.remove(self.length-1)
            self.length -= 1
            self.top = self.NodeList.tail
            return Popped.value
        else:
            print("\nReached bottom of stack, no objects to pop\n")
            self.top = self.NodeList.tail
            self.bottom = self.NodeList.head
            return None

class Stack2():
    def __init__(self,InitVal=None):
        self.StackList = []
        for x in range(0,MAX_STACK_LEN-1):
            self.StackList.append(x)
        
        self.top = None
        self.bottom = None
        self.length = 0
        
        if InitVal is not None:
            self.StackList[self.length] = InitVal
            self.top = InitVal
            self.bottom = InitVal
    
    def peek(self):
        return self.top
    
    def push(self,NewVal):
        
        if NewVal is not None:
            self.StackList[self.length] = NewVal
            if self.length == 0:          
                self.top = NewVal
                self.bottom = NewVal
            else:
                self.top = NewVal
            
            self.length += 1
    
    def pop(self):
        popped = None
        
        if self.length > 1:
            popped = self.top
            self.length -= 1
            self.top = self.StackList[self.length-1]
            
        elif self.length == 1:
            popped = self.top
            self.length = 0
            self.top = None
            self.bottom = None
        return popped
            

class Queue():
    def __init__(self,InitVal=None):
        self.length = 0
        self.List = LinkedLists.LinkedList_Single_Def(InitVal)
        self.top = self.List.head
        self.bottom = self.List.tail
        if InitVal is not None:
            self.length += 1
    
    def Queue(self,NewVal):
        self.List.append(NewVal)
        self.top = self.List.head
        self.bottom = self.List.tail
        self.length += 1
        return self.bottom
    
    def Dequeue(self):
        if self.length > 0:
            HoldingVal = self.List.head
            self.List.remove(0)
            self.top = self.List.head
            self.bottom = self.List.tail
            self.length -= 1
            return HoldingVal.value
        else:
            return None
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            