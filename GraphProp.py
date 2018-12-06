"""
Course: CS2302 Data Structures
Author: Javier Navarro
Assignment: Lab 6
Instructor: Diego Aguirre
TA: Manoj Saha
Last modified: 12/5/18
Purpose: Holds Vertex and Graph classes (GraphProperties)
"""

class Vertex:
    def __init__(self, label):
        self.label = label

class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}
    
    #adds a vertex to the adjacency list
    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []
    
    #adds edge to graph with direction 
    def add_directed_edge(self, from_vertex, to_vertex, weight = 1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)
    
    #adds edge to graph without direction
    def add_undirected_edge(self, vertex_a, vertex_b, weight = 1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)

    #looks for given vertex in the graph
    def get_vertex(self, vertex_label):
        for vertex in self.adjacency_list:
            if vertex.label == vertex_label:
                return vertex
        return None

    #returns list of all vertices in the graph
    def get_vertex_list(self):
        return list(self.adjacency_list)

    #returns list of incoming edges to a given vertex
    def get_incoming_edges(self, vertex):
        incoming = []
        for edge in self.edge_weights:
            if edge[1] is vertex:
                incoming.append(edge)
        return incoming
    
    #returns number of incoming edges to a given vertex
    def get_incoming_edge_count(edge_list, vertex):
        count = 0
        for (from_vertex, to_vertex) in edge_list:
            if to_vertex is vertex:
                count = count + 1
        return count