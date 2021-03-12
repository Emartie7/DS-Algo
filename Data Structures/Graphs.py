#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 20:01:29 2021

@author: emartie7
"""
#Implement a basic undirected, unweighted graph
class Graph:
    def __init__(self):
        self.NumNodes = 0
        self.adjacentList = {}
    
    #Add a node/vertex to the graph
    def addNode(self,NewNode=None):
        if NewNode is not None:
            self.adjacentList[NewNode] = [] #Initialize empty node with no connections
            self.NumNodes += 1
            return True
        
    #Add an edge/create connection
    def addEdge(self,Node1,Node2):
        if (Node1 is not None) and (Node2 is not None):
            # print("Forming connection between {} and {}".format(Node1,Node2))
            self.adjacentList[Node1].append(Node2)
            self.adjacentList[Node2].append(Node1)
    
    #Print the adjacency list for this graph
    def showConnections(self):
        for key in self.adjacentList:
            print(str(key) + " -> "+ " ".join(map(str,self.adjacentList[key])))
        
myGraph = Graph()
myGraph.addNode(0)
myGraph.addNode(1)
myGraph.addNode(2)
myGraph.addNode(3)
myGraph.addNode(4)
myGraph.addNode(5)
myGraph.addNode(6)
myGraph.addEdge(3,1)
myGraph.addEdge(3,4)
myGraph.addEdge(4,2)
myGraph.addEdge(4,5)
myGraph.addEdge(1,2)
myGraph.addEdge(1,0)
myGraph.addEdge(0,2)
myGraph.addEdge(6,5)
myGraph.showConnections()