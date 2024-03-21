class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graphDict = {}
        for start, end in self.edges:
            if start in self.graphDict:
                self.graphDict[start].append(end)
            else:
                self.graphDict[start] = [end]
        print(self.graphDict)     

    def getPaths(self, start, end, path = []):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graphDict:
            return []
        paths = []
        for node in self.graphDict[start]:
            newPaths = self.getPaths(node, end, path)
            for p in newPaths:
                paths.append(p)
        return paths 

    def getShortestPath(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graphDict:
            return None
        shortestPath = None
        for node in self.graphDict[start]:
            if node not in path:
                sp = self.getShortestPath(node, end, path)
                if shortestPath is None or len(sp) < len(shortestPath):
                    shortestPath = sp 
        return sp                              

if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Paris", "New York"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
    routeGraph = Graph(routes)
    start = "Mumbai"
    end = "New York"
    print(f"Paths between {start} and {end}: ", routeGraph.getPaths(start, end))
    print(f"Shorted Path between {start} and {end}: ", routeGraph.getShortestPath(start, end))
