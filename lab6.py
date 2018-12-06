"""
Course: CS2302 Data Structures
Author: Javier Navarro
Assignment: Lab 6
Instructor: Diego Aguirre
TA: Manoj Saha
Last modified: 12/5/18
Purpose: Topological Sort and Kruskals Algorithm
"""
import GraphProp
import dsf

def main():
    #creating graph using hash table and set
    graph1= {
            'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
            'edges': set([
            (15, 'A', 'B'),
            (6, 'A', 'D'),
            (9, 'B', 'C'),
            (12, 'B', 'D'),
            (14, 'B', 'G'),
            (10, 'B', 'H'),
            (16, 'C', 'E'),
            (8, 'D', 'E'),
            (6, 'E', 'F'),
            ])
    }
    
    print("\nAll edges in graph before Kruskal's Algorithm:")
    edges = list(graph1['edges']) #make list out of edges
    edges.sort()                  #sorts edges list
    #prints all edges with weights
    for i in range(len(edges)):
        print(edges[i][1], " --", edges[i][0], "-> ", edges[i][2])
    
    print()
    
    mst = kruskals_algorithm(graph1) #holds graph after kruskals
    print("Minimum spanning tree using Kruskal's Algorithm:")
    #prints all edges with weights
    for i in range(len(mst)):
        print(mst[i][1], " --", mst[i][0], "-> ", mst[i][2])
    
    graph2 = GraphProp.Graph()
    
    #creates vertices for graph
    vertex_A = GraphProp.Vertex('A')
    vertex_B = GraphProp.Vertex('B')
    vertex_C = GraphProp.Vertex('C')
    vertex_D = GraphProp.Vertex('D')
    vertex_E = GraphProp.Vertex('E')
    vertex_F = GraphProp.Vertex('F')
    vertex_G = GraphProp.Vertex('G')
    
    #adds all vertices to the graph
    graph2.add_vertex(vertex_A)
    graph2.add_vertex(vertex_B)
    graph2.add_vertex(vertex_C)
    graph2.add_vertex(vertex_D)
    graph2.add_vertex(vertex_E)
    graph2.add_vertex(vertex_F)
    graph2.add_vertex(vertex_G)
    
    #adds all directed edges
    graph2.add_directed_edge(vertex_A, vertex_B)
    graph2.add_directed_edge(vertex_A, vertex_C)
    graph2.add_directed_edge(vertex_B, vertex_F)
    graph2.add_directed_edge(vertex_C, vertex_D)
    graph2.add_directed_edge(vertex_D, vertex_F)
    graph2.add_directed_edge(vertex_E, vertex_F)
    graph2.add_directed_edge(vertex_E, vertex_G)
    graph2.add_directed_edge(vertex_F, vertex_G)
    
    
    
    
    print("\nAll edges in graph before topological sort:")
    #prints all edges
    for vertex in graph2.get_vertex_list():
        for pointers in graph2.get_incoming_edges(vertex):
            print(pointers[0].label, '-> ', end='')
            print(vertex.label, end='')
            print()

    print()
    
    result_list = topological_sort(graph2) #holds graph after topological sort
    
    print("Graph after topological sort:")
    first = True
    #prints all edges
    for vertex in result_list:
        if first:
            first = False
        else:
            print(' -> ', end='')
        print(vertex.label, end='')
    print()
    

def kruskals_algorithm(graph):
    dsf1 = dsf.DisjointSetForest()  #holds disjoint set forest
    
    for vertex in graph['vertices']:#makes each vertex into a set
        dsf1.make_set(vertex)
    
    minimum_spanning_tree = set()   #holds the tree to be returned
    edges = list(graph['edges'])    #list of all edges in the tree
    edges.sort()                    #sorts the edges
    
    for edge in edges:
        weight, vertice1, vertice2 = edge #assigns each var. to part of the edge set
        if dsf1.find(vertice1) != dsf1.find(vertice2):
            dsf1.union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
        	    
    return sorted(minimum_spanning_tree)

def topological_sort(graph):
    result_list = []    #holds list to be returned
    no_incoming = []    #holds vertices with indegree 0 
    
    for vertex in graph.adjacency_list.keys():
        if GraphProp.Graph.get_incoming_edge_count(graph.edge_weights.keys(), vertex) == 0:
            no_incoming.append(vertex)
    
    remaining_edges = set(graph.edge_weights.keys()) #starts with all edges
    while len(no_incoming) != 0: #loops until no more vertices with indegree 0
        current_vertex = no_incoming.pop()
        result_list.append(current_vertex)
        
        outgoing_edges = []

        #removes outgoing edges from remaining_edges
        for to_vertex in graph.adjacency_list[current_vertex]:
            outgoing_edge = (current_vertex, to_vertex)
            if outgoing_edge in remaining_edges:
                outgoing_edges.append(outgoing_edge)
                remaining_edges.remove(outgoing_edge)
                
        #checks if removing an edge creates a new vertex with indegree 0
        for (from_vertex, to_vertex) in outgoing_edges:
            in_count = GraphProp.Graph.get_incoming_edge_count(remaining_edges, to_vertex)
            if in_count == 0:
                no_incoming.append(to_vertex)
    
    return result_list
    
main()