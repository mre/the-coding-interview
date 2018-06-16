"""
    Length of SOURCE and TARGET words must be the same.

    This program uses the words.txt file in this same directory.
"""

class Vertex():
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.predecessor = None
        self.distance = 0
    
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight
        
    def getConnections(self):
        return [v for v in self.connectedTo.keys()]
    
    def getId(self):
        return self.id
    
    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def getDistance(self):
        return self.distance

    def setDistance(self, dis):
        self.distance = dis
    
    def setPred(self, v):
        self.predecessor = v
    
    def getPred(self):
        return self.predecessor
    
    
    
class Graph():
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    
    def addVertex(self,key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    def getVertex(self,key):
        return self.vertList[key]
    
    def __contains__(self,key):
        return key in self.vertList
    
    def __getitem__(self,key):
        return self.vertList[key]
    
    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nt = self.addVertex(t)
        
        self.vertList[f].addNeighbor(self.vertList[t],cost)
    
    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())


def buildGraph(g):
    d = {}
    with open("words.txt") as file:
        for word in file:
            word = word.replace("\n","")
            for i in range(len(word)):
                bucket = word[:i] + "_" + word[i+1:]
                if bucket not in d:
                    d[bucket] = [word]
                else:
                    d[bucket].append(word)

    for vertex in d.keys():
        for word in d[vertex]:
            for word2 in d[vertex]:
                if word != word2:
                    g.addEdge(word,word2)
    return g

def BFS(g, start, goal):
    visited = set() 
    queue = [start]
    visited.add(start)
    while len(queue) > 0:
        currentVert = queue.pop()
        visited.add(currentVert)
        for nbr in g[currentVert].getConnections():
            if nbr.id not in visited:
                g[nbr.id].setDistance(g[currentVert].getDistance() + 1)
                g[nbr.id].setPred(g[currentVert])
                visited.add(nbr.id)
                queue.insert(0,nbr.id)
    return visited

def traverse(g, start, goal):
    bfs = BFS(g,start, goal)
    path = []
    predecessor = g[goal].getPred()
    if start in bfs and goal in bfs:
        path.append(g[goal])
        while predecessor != None:
            path.append(predecessor)
            predecessor = predecessor.getPred()
    return reversed(path)

def main():
    GRAPH = Graph()
    g = buildGraph(GRAPH)
    print("Breadth First Search Word Ladder Algorithm!")
    print("="*43+"\n")

    try:
        a, b = input("Choose word1: "), input("Choose word2: ")
        c = traverse(g, a, b)
        print("\nPATH:")
        for v in c:
            print(v.id)
    except Exception as err:
        print("\nERROR: Cannot reach '{}' from start: '{}' based on our words.txt file.".format(b, a))


if __name__ == '__main__':
    main()