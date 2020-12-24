#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 20:17:10 2020

@author: emartie7
"""

def swap(arrayIn,index):
    x = arrayIn[index]
    arrayIn[index] = arrayIn[index+1]
    arrayIn[index+1] = x

def mergeSortedArrays(ArrayIn1, ArrayIn2):
    if not ArrayIn1:
        return ArrayIn2
    elif not ArrayIn2:
        return ArrayIn1
    
    mergedArray = ArrayIn1 + ArrayIn2
    
    for j in range(0,len(mergedArray)-2):
        
        for i in range(0,len(mergedArray)-1):
            if(mergedArray[i] > mergedArray[i+1]):
                swap(mergedArray,i)
    
    return mergedArray

newArray = mergeSortedArrays([0,3,4,31], [])    #Test using different arguments here
print(newArray)
