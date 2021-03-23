#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 20:29:36 2021

@author: emartie7
"""

#Factorial operation recursive
def FactorialRecursive(Value):
    if Value > 0:
        print("Current value is: {}".format(Value))
        product = Value * FactorialRecursive(Value-1)
        print("     Intermediate product is: {}".format(product))
        return product
    else:
        return(Value+1)
        

def FactorialIterative(Value):
    Product = 1
    for x in reversed(range(0,Value)):
        print("Current value is: {}".format(x))
        Product *= (x+1)
        print(Product)
    return Product

Result1 = FactorialRecursive(7)   #5040
Result2 = FactorialRecursive(0)   #0

Result3 = FactorialIterative(7) #5040
Result4 = FactorialIterative(0) #0