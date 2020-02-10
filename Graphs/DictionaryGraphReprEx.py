class Vertex(object):
    
    def __init__(self, label=''):
            self.label = label
            
    def __repr__(self):
        return 'Vertex(%s)' % repr(self.label)
    
    __str__ = __repr__
    
class Edge(tuple):

    def __new__(cls, e1, e2):
        return tuple.__new__(cls, (e1, e2))
    
    def __repr__(self):
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    __str__ = __repr__

class Graph(dict):
    
    def __init__(self, vs = [], es = []):
        
        for v in vs:
            self.add_vertex(v)
        for e in es:
            self.add_edge(e)
            
    def add_vertex(self, v):
        self[v] = {}
            
    def add_edge(self, e):
        v, w = e            
        self[v][w] = e
        self[w][v] = e
        
    def get_edge(self, v, w):
        
        try:
            print(self[v][w])
            return self[v][w]
        except:
            print("Edge not found")
            return None
        
    def remove_edge(self, v, w):
        try:
            del self[v][w]
            del self[w][v]
        except:
            print("Edge does not exist")
            
    def vertices(self):
        
        vertices = []
        for v in self.keys():
            vertices.append(v)
            
        print(*vertices)
        return vertices
    
    def edges(self):
        
        edges = []
        for e in self.values():
            if type(e) == dict:
                for inner_e in e.values():
                    edges.append(inner_e)
            else:
                edges.append(e)
            
#        print(*edges)
        return edges
    
    def reversed_edges(self):
        
        reversed_edges = []
        edges = self.edges()
        for e in edges:
            reversed_edges.append([e[1], e[0]])
            
#        print(*edges)
        return reversed_edges
    
    def out_vertices(self, v):
        
        adjacent = []
        for vertex, edge in self.items():
            if vertex == v:
                for adj_ver in edge.keys():
                    adjacent.append(adj_ver)
                
#        print(v, "is connected to the following vertices:")
#        print(*adjacent)
        return adjacent
    
    def out_edges(self, v):
        
        adjacent = []
        for vertex, edge in self.items():
            if vertex == v:
                for adj_ver in edge.values():
                    adjacent.append(adj_ver)
                
#        print(v, "has the following edges:")
#        print(*adjacent)
        return adjacent
    
    def add_all_edges(self):
        
        for vertex_out in self.keys():
            for vertex_in in self.keys():
                if vertex_in != vertex_out:
                    self.add_edge([vertex_in, vertex_out])
                    
    def add_regular_edges(self, k):
        """ n >= k + 1
            n*k%2 =0
            where k is the degree of the regular graph
                  n is the number of vertices
        """
        n = len(self.veritices())
        if n < (k+1):
            print("n < k + 1")
            raise Exception("Number of edges has to greater og equal to cardinality+1")
        elif (n*k)%2 != 0:
            print("n*k%2 != 0")
            raise Exception("Product of vertices and cardinality must be even")
        else:
            for vertex in self.keys():
                while len(self.out_edges(vertex)) < k:
                    for vertex_to_connect in self.keys():
                        if (vertex != vertex_to_connect) and ([vertex, vertex_to_connect] not in self.out_edges(vertex)):
                            self.add_edge(Edge(vertex, vertex_to_connect))
        
            
        
if __name__ == "__main__":        
    v = Vertex('v')
    w = Vertex('w')
    a = Vertex('a')
    e = Edge(v, w)
    e1 = Edge(v, a)
    
    g = Graph([v, w, a])
    g.add_all_edges()
    print(g)
        
