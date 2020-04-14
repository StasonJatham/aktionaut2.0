class AktionautSave:

	def save_symbols(self, symbols_list):
		# copy and paste that symbols function from all_ticker.py in here


	def save_prices(self, symbol, pd_price):
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

	def save_news(self, symbol, feed_title, feed_link, feed_published):
		# save news from RSS feeds to new table in AKTIONAUT.db
		# FIRST MATCH STORY TO SYMBOL

	# we will back up our AKTIONAUT.db here and no where else
	# zip AKTIONAUT.db for backup