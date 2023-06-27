from abc import ABC, abstractmethod

class pyTPS_Transaction(ABC):
    def doTransaction(self):
        pass

    def undoTransaction(self):
        pass
    
    def toString(self):
        pass
