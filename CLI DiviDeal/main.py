from user import *
from split import *
from expense import *
from expensetype import *
from expenseservice import *
from expensemanager import *
from FordFulkerson import *
import os
import json
from balance_sheet import *
from pots import *
from edit_participants import *
from items import *
import sqlite3
from simplify2 import*


def get_connection():
        connection  = sqlite3.connect("database.db")
        return connection
if __name__=='__main__':
    
    ExpenseManager=expensemanager()
    max_flow=simplify()
    
    db_balance_sheet = balancesheet()
    db_pot = pots()
    pot_id = 0
    connection = get_connection()
    
    ExpenseManager.adduser(User("u1", "User1", "gaurav@workat.tech", "9876543210"))
    ExpenseManager.adduser(User("u2", "User2", "sagar@workat.tech", "9876543210"))
    ExpenseManager.adduser(User("u3", "User3", "hi@workat.tech", "9876543210"))
    ExpenseManager.adduser(User("u4", "User4", "mock-interviews@workat.tech", "9876543210"))
    ExpenseManager.adduser(User("u5", "User5", "h@workat.tech", "9876543211"))
    ExpenseManager.adduser(User("u6", "User6", "moc-interviews@workat.tech", "8876543210"))
    ExpenseManager.adduser(User("u7", "User3", "hi@workat.tech", "9876543210"))
    ExpenseManager.adduser(User("u8", "User4", "mock-interviews@workat.tech", "9876543210"))
    ExpenseManager.adduser(User("u9", "User5", "h@workat.tech", "9876543211"))
    ExpenseManager.adduser(User("u10", "User6", "moc-interviews@workat.tech", "8876543210"))
    
    if(input("Enter OPEN or NEW: ") == "OPEN"):
        # for file in os.listdir("C:/Users/windows 10/Downloads/splitwise/splitwise"):
        #     if file.endswith(".db"):
        #         print(file)
        # expense_name = input("Enter any 1 filename: ")
        pots = db_pot.get_pots(connection)
        if len(pots) == 0:
            print("No pots exist- Create new pot-Enter new pot name")
        else:
            print(pots)
            pot_id = int(input("Give id of pot"))
            balancesheet = db_pot.getbalance(pot_id,connection)
            ExpenseManager.balancesheet = balancesheet
        # expenseManager.balanceSheet = prev_bal_sheet

    else:
        expense_name = input("Enter a new pot name: ")
        db_pot.set_pot(expense_name, "3480290sheiefiuv",connection)
        pot_id = db_pot.get_potid(expense_name,connection)
        participant_entry = database_entry()
        participant_entry.add_every_participant(pot_id[0],connection,ExpenseManager.usermap)
        pot_id = pot_id[0]
        
        
    while(1):
        commands=input().split()
        commandtype=commands[0]
        
        if(commandtype=="SHOW"):
            if(input("Want to simplify YES or NO:")=="YES"):
                #ExpenseManager.balancesheet=max_flow.final_simplify(ExpenseManager.balancesheet)
                #ExpenseManager.showbalance()
                ExpenseManager.balancesheet=simplify2.simplify(ExpenseManager.balancesheet)
            ExpenseManager.showbalance()
        
        elif(commandtype=="EXPENSE"):
            paidby=commands[1]
            amount=float(commands[2])
            noofusers=int(commands[3])
            expensetype=commands[4+noofusers]
            splits=[]
            
            
            if(expensetype=="EQUAL"):
               for i in range(0,noofusers):
                   splits.append(equalsplit(ExpenseManager.usermap.get(commands[4 + i])))
               ExpenseManager.addexpense(Expensetype[2], amount, paidby, splits,pot_id,connection)
              
            elif(expensetype=="EXACT"):
               for i in range(0,noofusers):
                   splits.append(Exactsplit(ExpenseManager.usermap.get(commands[4 + i]),float(commands[5 + noofusers + i])))
               ExpenseManager.addexpense(Expensetype[0], amount, paidby, splits,pot_id,connection)
               
               
            elif(expensetype=="PERCENT"):
               for i in range(0,noofusers):
                   splits.append(percentsplit(ExpenseManager.usermap.get(commands[4 + i]),float(commands[5 + noofusers + i])))
               ExpenseManager.addexpense(Expensetype[1], amount, paidby, splits,pot_id,connection)
              
                
            elif(expensetype=="SHARES"):
                for i in range(0,noofusers):
                    splits.append(sharesplit(ExpenseManager.usermap.get(commands[4+i]), float(commands[5+noofusers+i])))
                ExpenseManager.addexpense(Expensetype[3], amount, paidby, splits,pot_id,connection)
               

            elif(expensetype == "ADJUST"):
                for i in range(0,noofusers):
                    splits.append(adjustsplit(ExpenseManager.usermap.get(commands[4+i]), float(commands[5+noofusers+i])))
                ExpenseManager.addexpense(Expensetype[4], amount, paidby, splits,pot_id,connection)
                
            db_balance_sheet.update_balance_sheet(ExpenseManager.balancesheet,pot_id,connection)
            connection.commit()
            
        else:
            connection.close()
            break