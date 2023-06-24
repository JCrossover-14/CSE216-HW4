class pyTPS:
    
    def __init__(self,performingDo,performingUndo,mostRecentTransaction,transactions):
        self.performingDo = False
        self.performingUndo = False
        self.mostRecentTransaction = -1
        self.transactions = []
    
    def addTransaction(self,transaction):
        if self.mostRecentTransaction>0 or self.mostRecentTransaction<(len(self.transactions))-1:
            for i in range (len(self.transactions)-1,self.mostRecentTransaction,-1):
                del self.transactions[i]
        self.transactions.append(transaction)
        self.doTransaction()
    
    def doTransaction(self):
        if self.hasTransactionToRedo():
            self.performingDo = True
            transaction = self.transactions[self.mostRecentTransaction+1]
            transaction.doTransaction()
            self.mostRecentTransaction+=1
            self.performingDo = False
    
    def undoTransaction(self):
        if self.hasTransactionToUndo:
            transaction = self.transactions[self.mostRecentTransaction]
            transaction.undoTransaction()
            self.mostRecentTransaction-=1
            self.performingUnod = False

    def hasTransactionToRedo(self):
        if(self.mostRecentTransaction+1<len(self.transactions)):
            return True
        return False
    
    def hasTransactionToRedo(self):
        if(self.mostRecentTransaction+1<len(self.transactions)):
            return True
        return False
    
    def clearAllTransactions(self):
        self.transactions.clear()
        self.mostRecentTransaction=-1

    def toSring(self):
        result = "--Number of Transactions: "+str(len(self.transactions))+"\n"
        result+=("--Current Index on Stack: "+str(self.mostRecentTransaction)+"\n")
        result+="--Current Transaction Stack:\n"
        for i in range (self.mostRecentTransaction+1):
            transaction = self.transactions[i]
            result+=("----")
            result+=transaction.toString()
            result+="\n"
        return result

        