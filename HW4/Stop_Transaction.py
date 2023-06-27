from pyTPS import pyTPS
from WeightedGraph import WeightedGraph
from WeightedEdge import WeightedEdge
from pyTPS_Transaction import pyTPS_Transaction

class Stop_Transaction(pyTPS_Transaction):
    def __init__(self,stops,graph,stop,distances):
        super().__init__()
        self.stops = stops
        self.stop = stop
        self.graph = graph
        self.distances = distances

    def doTransaction(self):
        self.stops.append(self.stop)
        if(len(self.stops)>1):
            last = self.stops[len(self.stops)-1]
            seclast = self.stops[len(self.stops)-2]
            lastAirport = self.graph.getNodeData(last)
            secLastAirport = self.graph.getNodeData(seclast)
            distance = lastAirport.calculateDistance(lastAirport,secLastAirport)
            self.distances.push(distance)
    
    def undoTransaction(self):
        self.stops.pop()

    def toString(self):
        str = "Stops "
        for stop in self.stops:
            str+="-"
            str+=stop
        return str
    

