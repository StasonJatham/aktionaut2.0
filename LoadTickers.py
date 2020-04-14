import sqlite3

class LoadTickers:
	"""
	Returns a list of Tickers
	"""
	def load_symbol():
		connection = sqlite3.connect('./DB/AKTIONAUT.db')
		curs = connection.cursor()
		curs.execute('select symbol from symbols')
		tickers = curs.fetchall()
		# we gave to check if we get output as a list ---------> TEST THIS
		return tickers

	def load_name():
		connection = sqlite3.connect('./DB/AKTIONAUT.db')
		curs = connection.cursor()
		curs.execute('select name from symbols')
		names = curs.fetchall()
		# we gave to check if we get output as a list ---------> TEST THIS
		return names

