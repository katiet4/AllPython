import mysql.connector
class dataBase:
	def __init__(self,base:'database'):
		self.base = base
	def __enter__(self):
		self.conn = mysql.connector.connect(**self.base)
		self.cursor = self.conn.cursor()
		return self.cursor
	def __exit__(self,exc_type,exc_value,exc_trace):
		self.conn.commit()
		self.conn.close()
		self.cursor.close()