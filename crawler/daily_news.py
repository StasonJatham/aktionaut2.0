#!/usr/bin/env python3

import sys
sys.path.append("./Aktionautenlibs/")

import requests
import datetime
import feedparser



class news_RSS_all:

	# get date time, no clue if we need it but maybe
	now = datetime.datetime.now()
	todays_date = "{0}/{1}/{2}".format(now.year, now.month, now.day)

    def __init__(self):

    	# UNDER CONSTRUCTION --> MOVE TO LoadTickers
    	# will be replaced with  tickers = LoadTickers.load()
    	# we also want to laod names of companies to match if they
    	# are in the news stories
    	#################################################
		connection = sqlite3.connect('./DB/AKTIONAUT.db')
		curs = connection.cursor()
		curs.execute('select symbol from symbols')
		tickers = curs.fetchall()
		# we gave to check if we get output as a list ---------> TEST THIS


	def import_feed():
		# read links from file
		# iterate over links
		# we have to test how we get the entire list of rss feeds
		news_feed = feedparser.parse('http://feeds.reuters.com/reuters/topNews')
		news_title       = news_feed['feed']['title']
		news_link        = news_feed['feed']['link']
		news_description = news_feed['feed']['description']
		news_published   = news_feed['feed']['published']

		list_of_links = []
		list_of_links.add(news_link)

		return list_of_links

	def match_news_to_symbol(self, feed_link, company_symbol, company_name):
		# regex magic
		# return dataframe in format
		# 	id - symbol - feed_link
		pass


###### at this point in the code i should have:
				# a table in AKTIONAUT.db with news stories linked to companies


def main():

	# use this to test if our news db is working as intended
	connection = sqlite3.connect('./DB/AKTIONAUT.db')
	curs = connection.cursor()
	curs.execute('select symbol, title from companynews')
	test_news = curs.fetchall()
	# print some shit

	#if works move on with the hard part of the code..regex, parsing etc


    news_RSS_all()


if __name__ == "__main__":
    main()


































































"""


#!/usr/bin/env python3
import re
import urllib
import csv
import os
import sys
import time
import datetime

import numpy as np
from bs4 import BeautifulSoup
import urllib.request

# iterate all dates
#   iterate all tickers
#     repeatDowdload
#       save to ./input/data/news_date.csv

class news_Reuters:
    def __init__(self):
        fin = open('./input/tickerList.csv')

        filterList = set()
        try: # this is used when we restart a task
            fList = open('./input/finished.reuters')
            for l in fList:
                filterList.add(l.strip())
        except:
            pass

        # https://uk.reuters.com/info/disclaimer
        # e.g. http://www.reuters.com/finance/stocks/company-news/BIDU.O?date=09262017
        self.suffix = {'AMEX': '.A', 'NASDAQ': '.O', 'NYSE': '.N'}
        self.repeat_times = 4
        self.sleep_times = 2
        self.iterate_by_day(fin, filterList)


    def iterate_by_day(self, fin, filterList):
        dateList = self.dateGenerator(1) # look back on the past X days
        for timestamp in dateList: # iterate all possible days
            print("%s%s%s" % (''.join(['-'] * 50), timestamp, ''.join(['-'] * 50)))
            self.iterate_by_ticker(fin, filterList, timestamp)

    def iterate_by_ticker(self, fin, filterList, timestamp):
        for line in fin: # iterate all possible tickers
            line = line.strip().split(',')
            ticker, name, exchange, MarketCap = line
            #if ticker in filterList:
            #    continue
            if MarketCap == '0':
                continue
            print("%s - %s - %s - %s" % (ticker, name, exchange, MarketCap))
            self.repeatDownload(ticker, line, timestamp, exchange)

    def repeatDownload(self, ticker, line, timestamp, exchange):
        url = "https://www.reuters.com/finance/stocks/company-news/" + ticker + self.suffix[exchange]
        new_time = timestamp[4:] + timestamp[:4] # change 20151231 to 12312015 to match reuters format
        for _ in range(self.repeat_times):
            try:
                time.sleep(np.random.poisson(self.sleep_times))
                response = urllib.request.urlopen(url + "?date=" + new_time)
                data = response.read()
                soup = BeautifulSoup(data, "lxml")
                hasNews = self.parser(soup, line, ticker, timestamp)
                if hasNews:
                    return 1 # return if we get the news
                break # stop looping if the content is empty (no error)
            except: # repeat if http error appears
                print('Http error')
                continue
        return 0

    def parser(self, soup, line, ticker, timestamp):
        content = soup.find_all("div", {'class': ['topStory', 'feature']})
        if len(content) == 0: return 0
        fout = open('./input/news/' + timestamp[:4] + '/news_' + timestamp + '.csv', 'a+')
        for i in range(len(content)):
            title = content[i].h2.get_text().replace(",", " ").replace("\n", " ")
            body = content[i].p.get_text().replace(",", " ").replace("\n", " ")

            if i == 0 and len(soup.find_all("div", class_="topStory")) > 0:
                news_type = 'topStory'
            else:
                news_type = 'normal'

            print(ticker, timestamp, title, news_type)
            fout.write(','.join([ticker, line[1], timestamp, title, body, news_type]) + '\n')
        fout.close()
        return 1

    def dateGenerator(self, numdays): # generate N days until now
        base = datetime.datetime.today()
        date_list = [base - datetime.timedelta(days=x) for x in range(0, numdays)]
        for i in range(len(date_list)):
            date_list[i] = date_list[i].strftime("%Y%m%d")
        return date_list

def main():
    news_Reuters()

if __name__ == "__main__":
    main()


"""
