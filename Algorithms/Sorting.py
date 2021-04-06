#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 20:45:34 2021

@author: emartie7
"""
#############################################################################
##  Sorts numerical values utilizing the bubble sort algorithm
#############################################################################
def BubbleSort(ListIn):
    ListLen = len(ListIn)
    
    for x in reversed(range(0,ListLen)):    # [ListLen:0]
        for n in range(0,x):
            if ListIn[n] >  ListIn [n+1]:
                a = ListIn[n+1]
                ListIn[n+1] = ListIn[n]
                ListIn[n] = a
        print(ListIn)
    return ListIn
        
#############################################################################
##  Sorts numerical values utilizing the selection sort algorithm
##      This routine works as a sort of bubble sort algorithm but in reverse. 
##      The routine will iterate over the list, swapping the minimum value to
##      the "lowest" available index.
#############################################################################
def SelectionSort(ListIn):
    ListLen = len(ListIn)
    
    for idx in range(0,ListLen):
        MinVal = ListIn[idx]
        SwapIdx = idx
        for x in range(idx,ListLen):
            if ListIn[x] < MinVal:      #New minimum, perform swap
                MinVal = ListIn[x]
                SwapIdx = x
        a = ListIn[idx]
        ListIn[idx] = MinVal
        ListIn[SwapIdx] = a
        print(ListIn)
    return ListIn

#############################################################################
##  Sorts numerical values utilizing the selection sort algorithm
##      In this routine, the value at index "i" is the value the routine is
##      currently attempting to "place" in sorted order. The index "ii" is 
##      the new, destination index of the value ListIn[i]. In both cases 1+2, the
##      "current" value is popped from the list and then inserted into the new index "ii"
#############################################################################
def InsertionSort(ListIn):
    ListLen = len(ListIn)
    for i in range(0,ListLen):
        if ListIn[i] < ListIn[0]:       #Case 1 - New minimum value, prepend
            a = ListIn.pop(i)
            ListIn.insert(0,a)
        else:
            for ii in range(1,ListLen):     #Case 2 - Figure out where the heck this goes
                if ListIn[i] < ListIn[ii]:
                    a = ListIn.pop(i)
                    ListIn.insert(ii,a)
        print(ListIn)
    return ListIn
                    
                
    
            
        
        
        
myList = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print("Performing sort using bubble sort algorithm . . . \n")
BubbleSort(myList)
myList = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print("\n\nPerforming sort using selection sort algorithm . . . \n")
SelectionSort(myList)
myList = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print("\n\nPerforming sort using insertion sort algorithm . . . \n")
InsertionSort(myList)
