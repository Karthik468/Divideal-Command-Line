import sqlite3

class database_entry:

	# def get_connection(self):
	# 	connection = sqlite3.connect("database.db")
		
	# 	return connection
	
	def add_every_participant(self,pot_id,conn,userMap):
		curr = conn.cursor()
		for user in userMap:
			curr.execute("INSERT INTO participants(pot_id,participant_name,paid,consumed,net) VALUES(?,?,?,?,?)",(pot_id,user,'0','0','0'))

	def edit_entry(self,user_id,amount,transact_type,pot_id,conn):
		# conn = self.get_connection()
		cur = conn.cursor()
		query = """SELECT "1"
WHERE EXISTS(SELECT 1 FROM participants 
       WHERE participant_name = ? and pot_id= ?)"""
		check_cond = cur.execute(query,(user_id,pot_id)).fetchone()
		if transact_type=="ADD":
			if check_cond != None:
				values = cur.execute("SELECT * FROM participants WHERE participant_name = ? and pot_id = ?",(user_id,pot_id,)).fetchone()
				cur.execute("UPDATE participants SET paid= ?, net= ? WHERE participant_name= ?",(str(int(values[3])+int(amount)),str(int(values[3])+int(amount)-int(values[4])),user_id,))
			else:
				cur.execute("INSERT INTO participants (pot_id,participant_name, paid, consumed, net) VALUES (?,?, ?, ?, ?)",(pot_id,user_id,amount,'0',amount))

		elif transact_type == "DEDUCT":
			if check_cond != None:
				values = cur.execute("SELECT * FROM participants WHERE participant_name = ? and pot_id = ?",(user_id,pot_id,)).fetchone()
				cur.execute("UPDATE participants SET consumed= ?, net= ? WHERE participant_name= ?",(str(int(values[4])+int(amount)),str(int(values[3])-int(amount)-int(values[4])),user_id,))
			else:
				cur.execute("INSERT INTO participants (pot_id,participant_name, paid, consumed, net) VALUES (?,?, ?, ?, ?)",(pot_id,user_id,'0',amount,-amount))




if __name__ == "__main__":
	test = database_entry()

	test.edit_entry("SUCHITH","1000","ADD")

			