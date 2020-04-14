#!/usr/bin/env python3
"""
Download the ticker list from IEX and save as csv.
Output will be saved in TABLE: symbols
"""

import sys
sys.path.append("./Aktionautenlibs/")

import requests
import pandas
import sqlite3
from Zip import Zip


# ---------------------------------------- GET TICKERS START ------------------
def get_tickers():
	"""
	Get all tickers available on IEX,
	as well as format and save data to DataFrame
	"""
	url = "https://api.iextrading.com/1.0/ref-data/symbols"
	
	try:
		response = requests.get(url)
		if str(response.status_code) == "200":
			print("[UPDATE]: Downlaoding Tickers from iextrading API")
			json_stock_data = response.json()

			pd_stock = pandas.DataFrame(json_stock_data)
			# DataFrame Format
			#             date  iexId  isEnabled                       name    symbol    type
			# 0     2019-02-12      2       True   Agilent Technologies Inc.         A     cs

			print("[SUCCESS]: Downloaded {} symbols from IEX.".format(len(pd_stock.index)))

			return pd_stock

		else:
			print("[ERROR]: Download from IEX failed.")
			return "ERROR"
	except Exception as e:
		print("[ERROR]: {}".format(e))
		return "ERROR"
# ---------------------------------------- GET TICKERS END --------------------


# ---------------------------------------- DATA TO SQL START ------------------
def data_to_sql(pd_stock_frame):
	"""
	This function saves our downloaded symbols
	to the "symbols" table in AKTIONAUT.db
	"""
	# --------------------------------------------------------------------------

	db_name = "DB/AKTIONAUT.db"

	conn = sqlite3.connect(db_name) #TODO: Move to seperate container
	cur = conn.cursor()

	try:
		pd_stock_frame.to_sql("symbols", conn, schema=None, 
			if_exists='replace', index=True, 
			index_label=None, chunksize=None, 
			dtype=None, method=None)

		print("[UPDATE]: symbols in {0} was updated.".format(db_name))
	except Exception as e:
		print("[ERROR]: symbols update failed.")
		print(e)

	cur.close()
	conn.close()
# ---------------------------------------- DATA TO SQL END --------------------


# ----------------------------------------------- MAIN ------------------------
def main():
	pd_stocks = get_tickers()

	try:
		if type(pd_stocks) == "str":
			print("[ERROR]: Saving to DB into table symbols failed.")
		else:
			data_to_sql(pd_stocks)
			print("[SUCCESS]: Wrote {} symbols to \"symbols\" in AKTIONAUT.db".format(len(pd_stocks.index)))
			
			try:
				Zip("DB/AKTIONAUT.db","DB_BACKUP/db_backup").zip()
				print("[BACKUP]: made a backup of DB dir")
			except Exception as e:
				print("[FATAL ERROR]: Backup failed.")
				print(e)
				print("-----------------------------")

	except Exception as e:
		print("[FATAL ERROR]: Fatal Error in main()")
		print(e)
		print("------------------------------------")



if __name__ == "__main__":
	main()
# ----------------------------------------------- MAIN ------------------------