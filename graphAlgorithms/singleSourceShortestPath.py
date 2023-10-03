class Graph:
    def __init__(self,gdict = None):
        if gdict == None:
            gdict = {}
        self.gdict = gdict

    def bfs(self,start,end):
        queue = [start]
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for ajacent in self.gdict.get(node, []):
                new_path = list(path)
                new_path.append(ajacent)
                queue.append(new_path)