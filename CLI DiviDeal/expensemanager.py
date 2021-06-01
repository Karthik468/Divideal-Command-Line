from user import*
from split import*
from expense import*
from expensetype import*
from expenseservice import*
from edit_participants import*
from items import*
import sqlite3

class expensemanager:
    expenses=None
    usermap=None
    balancesheet=None
    
    def __init__(self):
        self.expenses=[]
        self.usermap={}
        self.balancesheet={}
    
    def adduser(self,user):
        self.usermap.__setitem__(user.getid(),user)
        self.balancesheet.__setitem__(user.getid(),{})
        
    def addexpense(self,extype,amount,paidby,splits,potid,conn):
        db_table = database_entry()
        db_table.edit_entry(paidby,amount,"ADD",potid,conn)
        item_name=input("Enter item of these EXPENSE:")
        items.add_items(potid,item_name,'ITEM',amount,paidby,conn)
        paidbydict = self.usermap.get(paidby)
        Expense=Expenseservice.createexpense(extype, amount, self.usermap.get(paidby), splits)
        self.expenses.append(Expense)
        
        for split in Expense.getsplits():
            paidTo = split.getuser().getid()
            db_table.edit_entry(paidTo,split.getAmount(),"DEDUCT",potid,conn)
            items.add_items(potid,item_name,'kk',split.getAmount(),paidTo,conn)
            balances =self.balancesheet.get(paidby)
            
            if (paidTo not in balances):
                balances.__setitem__(paidTo, 0.0)
                
            balances.__setitem__(paidTo, balances.get(paidTo) + split.getAmount())
            self.balancesheet.__setitem__(paidby, balances)
            balances = self.balancesheet.get(paidTo)
            
            if (paidby not in balances):
                balances.__setitem__(paidby, 0.0)
                
            balances.__setitem__(paidby, balances.get(paidby) - split.getAmount())
            self.balancesheet.__setitem__(paidTo, balances)    
    def showbalance(self):
        if(not bool(self.balancesheet)):
            print("No Balance")
        else:
            print(self.balancesheet)