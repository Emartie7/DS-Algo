# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def ReverseStr (StringIn, StringInLen):
    StringOut = []
    for c in reversed(StringIn):
        StringOut.append(c)
        
    return ''.join(StringOut)

myString = 'Some string that will be reversed'
newString = ReverseStr(myString, len(myString)-1)
print('Old String: {}; New String: {}'.format(myString,newString))
