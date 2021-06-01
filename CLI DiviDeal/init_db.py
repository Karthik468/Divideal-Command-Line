import sqlite3

connection = sqlite3.connect('database.db')

with open('settlement_schema.sql') as f:
    connection.executescript(f.read())

with open('pots.sql') as f:
    connection.executescript(f.read())

with open('schema.sql') as f:
    connection.executescript(f.read())
     
with open('items.sql') as f:
    connection.executescript(f.read())
    
with open('consumers.sql') as f:
    connection.executescript(f.read()) 

cur = connection.cursor()

#cur.execute("INSERT INTO participants (participant_name, paid, consumed, net) VALUES (?, ?, ?, ?)",
# 		('SUCHITH','0','0','0'))

#lists = cur.execute("SELECT item_id,consumer_name,amount FROM consumers").fetchall()
#lists2 = cur.execute("SELECT pot_id,description,amount,paidby FROM items").fetchall()
lists3=cur.execute("SELECT* FROM participants ").fetchall()
connection.commit()
connection.close()

#print("Consumer Table:",lists)
#print("Items Table:",lists2)
print(lists3)