import sqlite3

class items:
    
    def add_items(pot_id,item_name,item_type,amount,user_name,conn):
        curr=conn.cursor()
        if(item_type=='ITEM'):
            curr.execute("INSERT INTO items(pot_id,description,amount,paidby) VALUES(?,?,?,?)",(pot_id,item_name,amount,user_name))
        
        else:
             item_id=curr.execute("SELECT item_id FROM items WHERE description=?",(item_name,)).fetchone()
             curr.execute("INSERT INTO consumers(item_id,consumer_name,amount) VALUES(?,?,?)",(item_id[0],user_name,amount))