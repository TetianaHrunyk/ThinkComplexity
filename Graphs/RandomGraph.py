"""Erdős-Rényi model, denoted G ( n, p ) , which
generates graphs with n nodes, where the probability
is p that there is an edge between
any two nodes."""

from DictionaryGraphReprEx import Graph, Vertex, Edge
import random
import math
random.seed = 0

class RandomGraph(Graph):
    """probability p should be float p in range [0, 1]"""
    
    def add_random_edges(self, p):

        vertices_list = self.vertices()
        vertices = {}
        for vertex in vertices_list:
            vertices[vertex] = 0
            
        edges_to_create = math.ceil(p*(len(vertices_list) - 1))
        print(edges_to_create, "edges will be created for each node")
        
        for vertex in self.keys():
            while vertices[vertex] < edges_to_create:
                vertex_to_connect = random.choice(vertices_list)
                if (vertex != vertex_to_connect) and (vertices[vertex_to_connect] < edges_to_create):
                    self.add_edge(Edge(vertex, vertex_to_connect))
                    vertices[vertex] += 1
                    vertices[vertex_to_connect] += 1
                    
        print(vertices)
                
                
if __name__ == "__main__":        
    a = Vertex('a')
    b = Vertex('b')
    c = Vertex('c')
    d = Vertex('d')
    e = Vertex('e')
    f = Vertex('f')
    
    g = RandomGraph([a, b, c, d, e, f])
    g.add_random_edges(0.5)
#    print(g)