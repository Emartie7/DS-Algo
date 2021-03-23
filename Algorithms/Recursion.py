#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 20:29:36 2021

@author: emartie7
"""

# O(n)
def FactorialRecursive(Value):
    if Value > 0:
        print("Current value is: {}".format(Value))
        product = Value * FactorialRecursive(Value-1)
        print("     Intermediate product is: {}".format(product))
        return product
    else:
        return(Value+1)
        
# O(n)
def FactorialIterative(Value):
    Product = 1
    for x in reversed(range(0,Value)):
        print("Current value is: {}".format(x))
        Product *= (x+1)
        print(Product)
    return Product

# Result1 = FactorialRecursive(7)   #5040
# Result2 = FactorialRecursive(0)   #1

# Result3 = FactorialIterative(7) #5040
# Result4 = FactorialIterative(0) #1


# O(n^2)
def Fibonacci(Value):
    if Value < 2:
        return Value
    else:
        Sum  = Fibonacci(Value-1) + Fibonacci(Value-2)
        return Sum
        
mySum = Fibonacci(9)
mySum1 = Fibonacci(4)