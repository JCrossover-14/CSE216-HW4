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
    #still left to be implemented

def displayAirports():
    print("need to display airports")

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
        s = ""
        distance = 0.0
        path = []
        airportGraph.findPath(path,stops[i-1],stops[i])
        s+="\n"
        s+=path[0]
        for x in range(1,len[path]):
            s= s+"-"+path[x]
            distance +=airportGraph.getNodeData(path[x-1]).calculateDistance(airportGraph.getNodeData(path[x-1]),airportGraph.getNodeData(path[x]))
        print(s)
        print(" ("+distance+" Miles)\n")
        total+=distance
    print("\nTotal Trip Distance: " +str(total)+ " Miles\n")
    




initAllAirports()
keepGoing = True
while(keepGoing):
    displayAirports()
    displayCurrentTrip()
    displayMenu()
    entry = input("- ")
    if entry == "S":
        airport = input("")
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
print("GOOD BYE!! :((")



