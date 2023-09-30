from collections import defaultdict

class Graph:
    def __init__(self,numOfVertexes):
        self.graph = defaultdict(list)
        self.numOfVertexes = numOfVertexes
    
    def addVertex(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topologicalSortUtils(self,v, visited ,stack):
        visited.append(v)
        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSortUtils(i,visited,stack)
        stack.insert(0,v)
    def topologicalSort(self):
        visited = []
        stack = []
        for k in list(self.graph):
            if k not in visited:
                self.topologicalSortUtils(k,visited,stack)

        print(stack)

customGraph = Graph(8)
customGraph.addVertex("b","a")
customGraph.addVertex("c","d")
customGraph.addVertex("d","a")
customGraph.addVertex("g","d")
customGraph.addVertex("e","c")
customGraph.addVertex("j","e")
customGraph.topologicalSort()