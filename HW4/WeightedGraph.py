from WeightedEdge import WeightedEdge
import heapq
class WeightedGraph:
    def __init__(self):
        self.nodes={}
        self.edges={}

    def getKeys(self,keys):
        keys.clear()
        for key in self.nodes:
            keys.append(key)
        return keys
    
    def nodeExists(self,testNode):
        if testNode in self.nodes:
            return True
        return False
    
    def getEdgeId(self,node1,node2):
        return node1+"-"+node2
    
    def addNode(self,nodeId, nodeData):
        self.nodes[nodeId]=nodeData

    def getNodeData(self,nodeId):
        return self.nodes[nodeId]
    
    def addEdge(self,node1,node2,weight):
        edgeId = self.getEdgeId(node1,node2)
        edge = WeightedEdge(node1,node2,weight)
        self.edges[edgeId]=edge

    def removeEdge(self,node1,node2):
        edgeId = self.getEdgeId(node1,node2)
        del self.edges[edgeId]

    def hasNeighbor(self,node1,node2):
        edgeId = self.getEdgeId(node1,node2)
        if edgeId in self.edges:
            return True
        return False
    
    def getNeighborWeight(self,node1,node2):
        if self.hasNeighbor(node1,node2):
            edgeId = self.getEdgeId(node1,node2)
            return self.edges[edgeId].getWeight()
        return 0.0
    
    def findPath(self,path,node1,node2):
        print("Finding path from "+node1+" to " +node2)
        pq = []
        distances={}
        previous = {}
        unvisited = set()

        for node in self.nodes:
            distances[node]=float('inf')
            previous[node]=''
            unvisited.add(node)

        distances[node1]=0.0
        heapq.heappush(pq,(0.0,node1))

        while len(pq)>0:
            dist,current = heapq.heappop(pq)

            for neighborId in self.nodes:
                if self.hasNeighbor(current,neighborId):
                    weight = self.getNeighborWeight(current,neighborId)
                    if dist+weight<distances[neighborId]:
                        distances[neighborId]=dist+weight
                        previous[neighborId]=current
                        heapq.heappush(pq,(dist+weight,neighborId))
            
        if distances[node2] == float('inf'):
            return
            
        cur = node2
        while cur !=node1:
            path.insert(0,cur)
            cur = previous[cur]
            
        path.insert(0,node1)


    
