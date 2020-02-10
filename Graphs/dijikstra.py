import DictionaryGraphReprEx

class Dijikstra:
    
    def __init__(self, graph):
        self.queue = {}
        self.distances = {}
        self.graph = graph
        
    def infinite_distance(self):
        for vertrex in self.graph.vertices():
            self.distances[vertrex] = False
            
    def update(self, vertex, distance = 1):
        keys = list(self.queue.keys())
        vertices = self.graph.out_vertices(vertex)
        for v in vertices:
            if v in keys:
                self.queue[v] += distance
            else:
                self.queue[v] = distance
                
    
    def shortest_path(self, start, end):
        assert end in self.graph.vertices()
        self.infinite_distance()
        self.queue[start] = 0
        
        while len(self.queue) > 0:
            key = list(self.queue.keys())[0]
            distance = self.queue[key]
            del self.queue[key]
            self.distances[key] = distance
            self.update(key)
            
        return self.distances[end]
    
if __name__ == "__main__":        
    v = Vertex('v')
    w = Vertex('w')
    a = Vertex('a')
    e = Edge(v, w)
    e1 = Edge(v, a)
    
    g = Graph([v, w, a], [e, e1])
    print("Vertices: ")
    g.vertices()
    print("Edges: ")
    print(g.edges())
    
    d = Dijikstra(g)
    print(d.shortest_path(a, v))
        
