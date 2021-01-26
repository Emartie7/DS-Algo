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
        
