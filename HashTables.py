#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 18:47:53 2020

@author: emartie7
"""

class myUser:
    age = 54
    name = "Kylie"
    magic = True
    
    def scream(self):
        print('Boo muthafucka')
        
# Andre = myUser()
# Andre.scream()

class myHashTableDef():
    def __init__ (self,length):
        self.TableSize = length
        self.Arr = []
        for x in range(length):
            self.Arr.append([])
        
    def __hash(self,key):
        myHash = 0;
        for c in key:
            myHash = (myHash + ord(c)) % self.TableSize
        return myHash
    
    def set(self,key,keyVal):
        hashKey = self.__hash(key)
        if self.Arr[hashKey] is None:           
            self.Arr[hashKey].append((key,keyVal))
        else:
            self.Arr[hashKey].append((key,keyVal))
        
    def get(self,key):
        hashVal = self.__hash(key)
        if(self.Arr[hashVal]) is not None:
            for x in self.Arr[hashVal]:
                print(x)
        return key
    
    def keys(self):
        Success = []
        for entry in self.Arr:
            if entry is not None:
                for subentry in entry:
                    Success.append(subentry[0])
        return Success
    
testTable = myHashTableDef(15)
testTable.set("Apple", 500)
testTable.set("Banana", 211)
testTable.set("Orange", 13)
testTable.set("Pineapple",1300)
# print(testTable.keys())

######################################################

def myHash(key,myMod):
    myHash = 0;
    myHash = key % myMod
    # for c in key:
    #     myHash = (myHash + ord(c)) % myMod
    return myHash

def returnFirstRecurring(ArrayIn):
    keyArr = []
    ArrayInLen = len(ArrayIn)
    for x in range(ArrayInLen):
        keyArr.append(None)
        
    for key in ArrayIn:
        if(keyArr[myHash(key,ArrayInLen)]) is None:
            keyArr[myHash(key,ArrayInLen)] = 1
        else:
            return key
    return None;

def returnFirstRecurring2(ArrayIn):
    myDict = {}
    for x in ArrayIn:
        if x in myDict:
            return x
        else:
            myDict[x] = 1
        # print(myDict)
    return None

print(returnFirstRecurring([2,5,5,2,3,5,1,2,4]))
print(returnFirstRecurring2([2,1,1,2,3,5,1,2,4]))
print(returnFirstRecurring2([2,3,4,5]))
    