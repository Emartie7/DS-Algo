#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 17:35:11 2021

@author: emartie7
"""
from LinkedLists import LinkedList_Single_Def

MyList = LinkedList_Single_Def(1)
MyList.append(10)
MyList.append(16)
MyList.append(88)
MyList.PrintList()
MyList.reverse()
MyList.PrintList()