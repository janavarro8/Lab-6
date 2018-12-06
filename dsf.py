"""
Course: CS2302 Data Structures
Author: Javier Navarro
Assignment: Lab 6
Instructor: Diego Aguirre
TA: Manoj Saha
Last modified: 12/5/18
Purpose: Holds DisjointSetForest class
"""

class DisjointSetForest:
    def __init__(self):
        self.parent = dict()
        self.rank = dict()
        
    #Makes a vertex its own set    
    def make_set(self, vertex):
        self.parent[vertex] = vertex
        self.rank[vertex] = 0
    
    #searches for a given vertex in the dsf
    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]
    
    #merges the sets of the 2 given vertices
    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
            if self.rank[root1] == self.rank[root2]: 
                self.rank[root2] += 1