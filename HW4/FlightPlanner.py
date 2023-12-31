from Airport import Airport
from WeightedEdge import WeightedEdge
from WeightedGraph import WeightedGraph
from Stop_Transaction import Stop_Transaction
from pyTPS import pyTPS
from pyTPS_Transaction import pyTPS_Transaction
import json
tps = pyTPS()
print(tps.toString())

airportGraph = WeightedGraph()
distances = []

stops =[]

def initAllAirports():
    print("Need to init airports")
    airport_data = json.load(open('Airports.json'))
    for airport in airport_data:
        port = Airport(airport["Airport"],airport["LatDegrees"],airport["LatMinutes"],airport["LongDegrees"],airport["LongMinutes"])
        airportGraph.addNode(port.getCode(),port)

    edge_data = json.load(open('Edges.json'))
    for edge in edge_data:
        a1 = airportGraph.getNodeData(edge["node1"])
        a2 = airportGraph.getNodeData(edge["node2"])
        distance = a1.calculateDistance(a1,a2)
        airportGraph.addEdge(a1.getCode(),a2.getCode(),distance)
        airportGraph.addEdge(a2.getCode(),a1.getCode(),distance)

    #still left to be implemented

def displayAirports():
    print("")
    print("AIRPORTS YOU CAN TRAVEL TO AND FROM:\n")
    s = ""
    codes = []
    airportGraph.getKeys(codes)
    for i in range (len(codes)):
        if i%10 == 0:
            s+="\t"
        s+=codes[i]
        if i<len(codes)-1:
            s+=", "
        if i%10==9:
            s+="\n"
    print(s+"\n")



def displayMenu():
    print("ENTER A SELECTION")
    print("S) Add a Stop to your Trip")
    print("U) Undo")
    print("R) Redo")
    print("E) Empty Trip")
    print("Q) Quit")

def displayCurrentTrip():
    print("Trip Stops: ")
    s = ""
    for i in range (len(stops)):
        s= s+"  "+str(i+1)+". "+stops[i]
    print(s)
    print("\n")
    print("Trip Legs: ")
    path = []
    total = 0.0
    for i in range(1,len(stops)):
        s = str(i)+"). "
        distance = 0.0
        path = []
        airportGraph.findPath(path,stops[i-1],stops[i])
        s+=path[0]
        for x in range(1,len(path)):
            s= s+"-"+path[x]
            distance +=airportGraph.getNodeData(path[x-1]).calculateDistance(airportGraph.getNodeData(path[x-1]),airportGraph.getNodeData(path[x]))
        print(s)
        print(" ("+str(distance)+" Miles)\n")
        total+=distance
    print("\nTotal Trip Distance: " +str(total)+ " Miles\n")
    




initAllAirports()
keepGoing = True
while(keepGoing):
    displayAirports()
    displayMenu()
    entry = input("- ")
    if entry == "S":
        airport = input("Enter your destination: ")
        stop = Stop_Transaction(stops,airportGraph,airport,distances)
        tps.addTransaction(stop)
    elif entry == "U":
        tps.undoTransaction()
    elif entry == "R":
        tps.doTransaction()
    elif entry == "E":
        stops = []
        tps.clearAllTransactions()
    elif entry=="Q":
        keepGoing = False
    displayCurrentTrip()
print("GOOD BYE!! :((")



