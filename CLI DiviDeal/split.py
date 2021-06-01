from user import*

class split:
    _user=None
    Amount=None;
    
    def __init__(self,user):
        self._user=user
        
    def setuser(self,user):
        self._user=user
        
    def setAmount(self,amount):
        self.Amount=amount
    
    def getuser(self):
        return self._user
        
    def getAmount(self):
        return self.Amount
    
class equalsplit(split):
    
    def __init__(self,user):
        super().__init__(user)

class Exactsplit(split):
    
    def __init__(self,user,amount):
        super().__init__(user)
        self.Amount=amount

class percentsplit(split):
    percent=None
    def __init__(self,user,percent):
        super().__init__(user)
        self.percent=percent
        
    def setpercent(self,Percent):
        self.percent=percent
    
    def getpercent(self):
        return self.percent

class sharesplit(split):
    share=None
    def __init__(self,user,share):
        super().__init__(user)
        self.share=share
    
    def setshare(self,share):
        self.share=share
        
    def getshare(self):
        return self.share

class adjustsplit(split):
    adjust=None
    def __init__(self,user,adjust):
        super().__init__(user)
        self.adjust=adjust
    
    def setadjust(self,adjust):
        self.adjust=adjust
        
    def getadjust(self):
        return self.adjust
    