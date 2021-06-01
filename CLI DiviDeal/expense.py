from user import*
from split import*

class expense:
    __id=None
    __Amount=None
    __paidby=None
    __splits=[]
    
    def __init__(self,amount,paidBy,Splits):
        #self.__id=idx
        self.__Amount=amount
        self.__paidby=paidBy
        self.__splits=Splits
    
    def setid(self,idx):
        self.__id=idx
        
    def setAmount(self,amount):
        self.__Amount=amount
        
    def setpaidby(self,paidBy):
        self.__paidby=paidBy
        
    def setsplits(self,Splits):
        self.__splits=Splits

    def getid(self):
        return self.__id
        
    def getAmount(self):
        return self.__Amount
        
    def getpaidby(self):
        return self.__paidby
        
    def getsplits(self):
        return self.__splits
    
class equalexpense(expense):
    
    def __init__(self,amount,paidBy,Splits):
        super().__init__(amount,paidBy,Splits)
        
class exactexpense(expense):
    
    def __init__(self,amount,paidBy,Splits):
        super().__init__(amount,paidBy,Splits)
        
class percentexpense(expense):
    
    def __init__(self,amount,paidBy,Splits):
        super().__init__(amount,paidBy,Splits)

class SharesExpense(expense):

    def __init__(self, amount, paidby, splits):
        super().__init__(amount, paidby, splits)


class AdjustExpense(expense):

    def __init__(self, amount, paidby, splits):
        super().__init__(amount, paidby, splits)
