# Edge List
graph=[[0,2],[2,3],[2,1],[1,3]]

#Adjacent List
graph=[[2],[2,3],[0,1,3],[1,2]]


#Adjacent Matrix
graph={
    0:[0,0,1,0],
    1:[0,0,1,1],
    2:[1,1,0,1],
    3:[0,1,1,0]
}


class Graph:
    def __init__(self):
        self.numberOfNodes=0
        self.adjacentList={}
    
    def addVertex(self,node):
        self.adjacentList[node]=[]
        self.numberOfNodes+=1

    def addEdge(self,node1,node2):
        if node1 not in self.adjacentList:
            self.addVertex(node1)
        if node2 not in self.adjacentList:
            self.addVertex(node2)
        
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)

    def showConnections(self):
        allNodes= self.adjacentList.keys()
        for node in allNodes:
            nodeConnections=self.adjacentList[node]
            connections=""
            for vertex in nodeConnections:
                connections += str(vertex) + " "
            print(node, " --> " + connections)
myG= Graph()
myG.addVertex(0)
myG.addVertex(1)
myG.addVertex(2)
myG.addVertex(3)
myG.addVertex(4)
myG.addVertex(5)
myG.addVertex(6)

myG.addEdge(3,1)
myG.addEdge(3,4)
myG.addEdge(4,2)
myG.addEdge(4,5)
myG.addEdge(1,2)
myG.addEdge(1,0)
myG.addEdge(0,2)
myG.addEdge(6,5)

myG.showConnections()