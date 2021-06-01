class User:
    __id=None
    __name=None
    __email=None
    __phone=None
    
    def __init__(self,idx,name1,email1,phone1):
        self.__id=idx
        self.__name=name1
        self.__email=email1
        self.__pone=phone1
    
    def setid(self,idx):
        self.__id=idx
    
    def setname(self,name1):
        self.__name=name1
    
    def setemail(self,email1):
        self.__email=email1
    
    def setphone(self,phone1):
        self.__phone=phone1
    
    def getid(self):
        return self.__id
        
    def getname(self):
        return self.__name
    
    def getemail(self):
        return self.__email
        
    def getphone(self):
        return self.__phone
    
    