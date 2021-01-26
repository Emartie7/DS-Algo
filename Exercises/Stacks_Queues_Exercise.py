#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 18:14:37 2021

@author: emartie7
"""

from Stacks_Queues import Stack

myStack = Stack(5)
print("\nTop value is: {}, length is: {}".format(myStack.top.value,myStack.length))
myStack.push(8)
myStack.push(15)
myStack.push(103)
myStack.push(78)
print("\nTop value is: {}, length is: {}".format(myStack.peek(),myStack.length))
# # print("\nPopping value: {}".format(myStack.pop()))
# # myStack.pop()
# print("\nTop value is: {}, length is: {}".format(myStack.top.value,myStack.length))

popped = 0
while popped is not None:
    popped = myStack.pop()
    print("\nPopped Value: {}; New length is: {}".format(popped,myStack.length))

print("\nTop value is: {}, bottom value is: {}".format(myStack.top.value,myStack.bottom))