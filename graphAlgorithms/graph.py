class Graph:
    def __init__(self,graphDict= None):
        if graphDict is None:
            graphDict = {}
        self.graphDict= graphDict
    
    def addEdge(self,vertex,edge):
        self.graphDict[vertex].append(edge)

    def bfs(self,vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            deVertex = queue.pop(0)
            print(deVertex)
            for adjacentVertex in self.graphDict[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)


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
graph.addEdge("e","g")
print(graph.graphDict)
graph.bfs("a")