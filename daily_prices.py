# TODO:
# - test GET_TICKERS()
# - create tables in AKTIOANUT.db aapl_data , goog_data....
# - write price data to table
# - make sure that only new data gets loaded into the database(primary key date)
#
# - test get tickers
# - test save_daily_price
# - test save_data_to_sql
# - add zip functiona t end
#
#
# - add more data to tables
# example: table aapl = columns --> date pe pb sales ....


import sys
sys.path.append("./Aktionautenlibs/")


#!/usr/bin/env python3
import pandas
import requests
import time



# read symbols from DB
def get_tickers():
	"""
	reads all symbols from symbols table in AKTIONAUT.db
	"""
	try:
		# UNDER CONSTRUCTION --> MOVE TO LoadTickers
		connection = sqlite3.connect('./DB/AKTIONAUT.db')
		curs = connection.cursor()
		curs.execute('select symbol from symbols')
		tickers = curs.fetchall()
		# we gave to check if we get output as a list ---------> TEST THIS
	    return(tickers)
	except Exception as e:
		print("[ERROR]: Could not load ticker symbols from AKTIONAUT.db")
		print("[ERROR]: {}".format(e))
		return "ERROR"


def save_daily_price(tickers):
	"""
	downlaods 5 year daily prices of all possible stocks and pairs from IEX
	and write it into AKTIONAUT.db xyz_data tables
	ONLY adds new data to table
	"""

	# format of the dataframe and table
	# {"date":"2014-02-13","open":70.2179,"high":71.5562,"low":70.1575,"close":71.501,"volume":76960156,"unadjustedVolume":10994308,"change":1.1176,"changePercent":1.588,"vwap":71.1055,"label":"Feb 13, 14","changeOverTime":0}
 	url = "https://api.iextrading.com/1.0/stock/{}/chart/5y".format(stock_symbol)
 	response = requests.get(url)
    try:
    	if response.status_code == 200:
	    	print("[UPDATE]: Downloading 5 year daily prices from iextrading API")
			json_stock_prices = response.json()
			pd_price = pandas.DataFrame(json_stock_prices)

			return pd_price
		else:
			print("[ERROR]: Download from IEX failed.")
			return "ERROR"
    except Exception as e:
    	print("[ERROR]: Download from IEX failed.")
    	print("[ERROR]: {}".format(e))
    	return "ERROR"

# UNDER CONSTRUCTION --> WILL BE MOVED TO AktionautSave
def save_data_to_sql(symbol, pd_price):
	# create table with {} .format(symbol)
	# create table columns that match dataframe (and more)
	# pd_price dataframe with data
	# write data to table
	# check that only new data is added to table

	# TABLE COLUMNS
	"""
	"date" #primary key
	"open"
	"high"
	"low"
	"close"
	"volume"
	"unadjustedVolume"
	"change"
	"changePercent"
	"vwap"
	"label"
	"changeOverTime"
	"""


def main():
	"""
	load ticker symbols
	iterate over ticker list
	download daily prices 5years from IEX API
	save to AKTIONAUT.db xyz_data table
	zip AKTIONAUT.db as backup
	"""
	tickers = get_tickers()
	for stock_symbol in tickers:
		daily_prices = save_daily_price(tickers)
		save_data_to_sql(stock_symbol, daily_prices)


if __name__ == "__main__":
    main()
