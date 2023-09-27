class Graph:
    def __init__(self,graphDict= None):
        if graphDict is None:
            graphDict = {}
        self.graphDict= graphDict
    
    def addEdge(self,vertex,edge):
        self.grahpDict[vertex].append(edge)


customDict = {
    "a":["c","d"],
    "b":["a","b","e"],
    "c":["f","b","e","a"],
    "d":["g","b"],
    "e":["f"],
    "f":["a","b"],
    "g":["c"],
}

graph = Graph(customDict)
print(graph.graphDict)