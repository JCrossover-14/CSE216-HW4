from Airport import Airport
from WeightedEdge import WeightedEdge
from WeightedGraph import WeightedGraph
from Stop_Transaction import Stop_Transaction
from pyTPS import pyTPS
from pyTPS_Transaction import pyTPS_Transaction

def initAllAirports():
    return
    #still left to be implemented

def displayAirports():
    return 

def displayMenu():
    return

def displayCurrentTrip():
    return 



tps = pyTPS()
print(tps.toString())

airportGraph = WeightedGraph()
distances = []

stops =[]
initAllAirports()
keepGoing = True
while(keepGoing):
    displayAirports()
    displayCurrentTrip()
    displayMenu()
    entry = input("- ")
    if entry == "S":
        airport = input("")
        stop = Stop_Transaction(stops,airport,airportGraph,distances)
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



