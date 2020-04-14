# Aktionaut 2.0
![AktionautLogo](marketing/Aktionaut.jpg)

Use natural-language processing (NLP) to predict stock price movement.
Based on the Projekt here: https://github.com/WayneDW/Sentiment-Analysis-in-Event-Driven-Stock-Price-Movement-Prediction

Some more linkl we will probly use 
http://francescopochetti.com/scrapying-around-web/
https://medium.com/mlreview/a-simple-deep-learning-model-for-stock-price-prediction-using-tensorflow-30505541d877
https://www.datacamp.com/community/tutorials/lstm-python-stock-market


This is the source where we found most of our base code:
```bash
https://github.com/topics/stock-price-prediction?l=python
```

Links to use for getting cool news:
```bash

Business Wire:
https://feed.businesswire.com/rss/home/?rss=G1QFDERJXkJeEFtRWA==
https://feed.businesswire.com/rss/home/?rss=G1QFDERJXkJeEFtRWQ==
https://feed.businesswire.com/rss/home/?rss=G1QFDERJXkJeEFtRXg==
https://feed.businesswire.com/rss/home/?rss=G1QFDERJXkJeEF9YXQ==
https://feed.businesswire.com/rss/home/?rss=G1QFDERJXkJeEFtRXw==
https://feed.businesswire.com/rss/home/?rss=G1QFDERJXkJeGVtWWQ==
https://feed.businesswire.com/rss/home/?rss=G1QFDERJXkJeEF9YXA==
https://feed.businesswire.com/rss/home/?rss=G1QFDERJXkJeEF9ZVA==
https://feed.businesswire.com/rss/home/?rss=G1QFDERJXkJeGVtYWQ==
https://feed.businesswire.com/rss/home/?rss=G1QFDERJXkJeEF5XWw==
https://feed.businesswire.com/rss/home/?rss=G1QFDERJXkJeGVtVVQ==
https://feed.businesswire.com/rss/home/?rss=G1QFDERJXkJeEFpRWw==
https://feed.businesswire.com/rss/home/?rss=G1QFDERJXkJeGVtWXA==
https://feed.businesswire.com/rss/home/?rss=G1QFDERJXkJeGVtXVA==


Benzinga Feeds:
http://articlefeeds.nasdaq.com/nasdaq/categories?category=Investing+Ideas	
https://www.cnbc.com/id/15839135/device/rss/rss.html	
http://feeds.benzinga.com/benzinga/news/guidance	
http://feeds.benzinga.com/benzinga/news/rumors		
http://feeds.benzinga.com/benzinga/news/insider-trades	
http://feeds.benzinga.com/benzinga/news/stock-split	
http://feeds.benzinga.com/benzinga/analyst-ratings/upgrades	
http://feeds.benzinga.com/benzinga/analyst-ratings/downgrades	
http://feeds.feedburner.com/Csimarket-EarningsReports
```


## TODO:
   | Current File                | Needs too happen | Status |
   | --------------------------- | ---------------- | ------ |
   | add file|add a Dockerfile for automatic build in Docker|
   | yahoo data | https://iextrading.com/developer/|
   | havent checked|check wordlist of positve and negative and add some|
   | make text file |add news sources (the ones we use in google sheets)|
   | ~~UPDATE: all_tickers.py~~ | ~~get tickers from IEX API~~| DONE
   | UPDATE: daily_prices.py  | get daily prices from IEX API|
   | UPDATE: daily_reuters.py | RSS feed stories of all our news sources, reuters link is hard coded|	   
   | UPDATE: reuters.py | get all the news for a ticker, we will rewrite this to store historical news headlines, and BUY or SELL rating with sql |
   | UPDATE: yahoo_finance.py | use IEX and IF needed we will still use this for long term hist data |
   | DELETE: yqd.py           | we will embed needed code in yahoo_finance.py |


## More TODO

TODO:

 example of Company bases rss feed from yahoo, may be interesting
 https://feeds.finance.yahoo.com/rss/2.0/headline?s=goog&region=US&lang=en-US


all_tickers.py

 TODO:
 - move save_to_sql into our lib SaveToSQL --> check SaveToSQL.py for a how to




daily_prices.py

 TODO:
 - test GET_TICKERS()
 - create tables in AKTIOANUT.db aapl_data , goog_data....
 - write price data to table
 - make sure that only new data gets loaded into the database(primary key date)
 - move function savetosql to lib
 - test get tickers
 - test save_daily_price
 - test save_data_to_sql
 - add zip functiona t end


 - add more data to tables
 example: table aapl = columns --> date pe pb sales ....



daily_news.py

 TODO:
 - add a news_sources.txt with all the RSS FEEDS
 - instead of looking for NEWS by SYMBOL we look for
   ALL NEWS and ,atch SYMBOLS to them
 - match news story to compnay before saving them
 - match news story to company in import_feedS()
 - match_news_to_symbol --> function to do the above point



 CHANGES
 daily_reuter.py --> daily_news.py
 class news_Reuters --> news_RSS_all
 delete reuters.py ---> same as this file --------------------> TODO
 delete yahoo_finance.py --------------------> TODO
 delte yqd.py --------------------> TODO



LoadTickers.py

 TODO:
 - test the laod functions
 - this should handle ALL loading data from SQL
   (symbol, name, news, pricing data, etc.)



SaveToSQL.py
 TODO:
 - clean allt he save to functioons
   from all the other files(as described ein their to dos)
 - move the create db and create table things into here
 - should handle all saving to sql functionality



## Methodology

1. Data Collection and Preprocessing

    1.1 crawl a ticker list to obtain the details of public companies

    1.2 crawl news from Reuters using BeautifulSoup
    
    1.3 crawl prices using urllib

2. Feature Engineering (Tokenization)
  
    2.1 Unify word format: unify tense, singular & plural, remove punctuations & stop words
  
    2.2 Implement one-hot encoding
  
    2.3 Pad word sequence (essentially a matrix) to keep the same dimension
  
3. Train a set of Bayesian Convolutional Neural Networks using Stochastic Gradient Langevin Dynamics to obtain more robustness
4. Use thinning models to predict future news

## Requirement
* Python 3
* Anaconda3 (has most of the requirements)
* [PyTorch > 0.4](https://pytorch.org/)
* numpy
* [NLTK](https://www.nltk.org/install.html)
* Crawler tools
  - pip3 install lxml
  - pip3 install bs4
  - pip3 install urllib

## Usage

Note: If you don't want to take time to crawl data and train the model, you can also directly go to step 4.

### 1. Data collection


#### 1.1 Download the ticker list from [NASDAQ](http://www.nasdaq.com/screening/companies-by-industry.aspx)

```bash
$ ./crawler/all_tickers.py 20  # keep the top e.g. 20% marketcap companies
```

#### 1.2 Use BeautifulSoup to crawl news headlines from [Reuters](http://www.reuters.com/finance/stocks/overview?symbol=FB.O)

*Note: you may need over one month to fetch the news you want.*

Suppose we find a piece of news about COO Lu Qi Resignation on May.18, 2018 at reuters.com

![](./imgs/baidu.PNG)

We can use the following script to crawl it and format it to our local file

```bash
$ ./crawler/reuters.py # we can relate the news with company and date, this is more precise than Bloomberg News
```

![](./imgs/111.png)

By brute-force iterating company tickers and dates, we can get the dataset with roughly 400,000 news in the end. Since a company may have multiple news in a single day, the current version will only use topStory news to train our models and ignore the others.

#### 1.3 Use urllib to crawl historical stock prices
 
Improvement here, use normalized return [5] over S&P 500 instead of return.

```bash
$ ./crawler/yahoo_finance.py # generate raw data: stockPrices_raw.json, containing open, close, ..., adjClose
$ ./create_label.py # use raw price data to generate stockReturns.json
```

### 2. Feature engineering (Tokenization)

Unify the word format, project word to a word vector, so every sentence results in a matrix.

Detail about unifying word format are: lower case, remove punctuation, get rid of stop words, unify tense and singular & plural.

```bash
$ ./tokenize_news.py
```

### 3. Train a Bayesian ConvNet to predict the stock price movement. 

Type the following to train a set of robust Bayesian models.
```bash
$ ./main.py -epochs 500 -static False
```

### 4. Prediction and analysis

Let's show one example how the thinning models react to Baidu Lu Qi's resignation
```bash
$ ./main.py -predict "Top executive behind Baidu's artificial intelligence drive steps aside"
>> Sell
```
The prediction makes sense, let's find another one.

```
Eli Lilly and Co (LLY.N)
FRI, JUN 1 2018
UPDATE 2-Lilly gets U.S. nod for arthritis drug, sets price well below rivals
* Drug priced at $25,000/year, 60 pct lower to AbbVie's Humira
```

```bash
$ ./main.py -predict "UPDATE 2-Lilly gets U.S. nod for arthritis drug  sets price well below rivals"
>> Sell
```

Lowering down drug prices looks helpful to gain market share in the business, however, they didn't mention too much about the updates of technology, we are inclined to regard it as the virulent price competition, which does not help to the company earnings. Thus it is not a bad decision to sell Eli Lilly stocks.

Next, let's see what the buy options look like:

```
Alphabet Inc (GOOG.O)
WED, MAY 30 2018
Google launches the second app in China, woos top smartphone market
* BEIJING Alphabet Inc's Google has launched a file managing tool in several Chinese app stores as it 
* looks for fresh inroads into the world's biggest smartphone market, where most of the internet 
* giant's top products remain banned.
```

```bash
$ ./main.py -predict "Google launches the second app in China  woos top smartphone market"
>> Strong Buy
```

By now, you have basically understood how the models work, let's use backtesting to examine the performance on the news in the past two weeks.
```bash
$ ./main.py -eval True
>> Testing    - loss: 0.6761  acc: 58.07%(41.8/72.0) 83.50%(3.3/3.9) 100.00%(0.0/0.0) 0.00%(0.0/0.0) 
```
Note: the predictions are averaged, which explains why we have float numbers. From left to right, the predictions become more and more confident. 58% is actually much higher than my expectation, I believe when tested on a longer time horizon, the performance gets worse. However, as long as the predictions are better than random guesses (50%), you can't lose money betting on a favorable game (assume no trading cost and liquidity issue).


### 5. Future works

This is a very rough work. Actually, a better label should be based on the comparison of stock price changes between the company and the corresponding industry, instead of the S&P 500. The idea is similar to hedging, a good investor doesn't have to be capable to predict the stock price change, as long as he knows what specific company does well in the specific industry, he will make a decent prediction.

From the [work](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1331573) by Tim Loughran and Bill McDonald, some words have a strong indication of positive and negative effects in finance, e.g. company merger and acquisition, we may need to dig into these words to find more information. In addition, detailed analysis and comparison in each industry are also useful.

Another simple but interesting example can be found in [Financial Sentiment Analysis part1](http://francescopochetti.com/scrapying-around-web/), [part2](http://francescopochetti.com/financial-blogs-sentiment-analysis-part-crawling-web/). 

Since a comprehensive stopword list is quite helpful in improving the prediction power, you are very welcome to build a better stopword list and share it.


## References:

1. Yoon Kim, [Convolutional Neural Networks for Sentence Classification](http://www.aclweb.org/anthology/D14-1181), EMNLP, 2014
2. J Pennington, R Socher, CD Manning, [GloVe: Global Vectors for Word Representation](http://www-nlp.stanford.edu/pubs/glove.pdf), EMNLP, 2014
3. Max Welling, Yee Whye Teh, [Bayesian Learning via Stochastic Gradient Langevin Dynamics](https://pdfs.semanticscholar.org/aeed/631d6a84100b5e9a021ec1914095c66de415.pdf), ICML, 2011
4. Tim Loughran and Bill McDonald, 2011, “When is a Liability not a Liability?  Textual Analysis, Dictionaries, and 10-Ks,” Journal of Finance, 66:1, 35-65.
5. H Lee, etc, [On the Importance of Text Analysis for Stock Price Prediction](http://nlp.stanford.edu/pubs/lrec2014-stock.pdf), LREC, 2014
6. Xiao Ding, [Deep Learning for Event-Driven Stock Prediction](http://ijcai.org/Proceedings/15/Papers/329.pdf), IJCAI2015
7. [IMPLEMENTING A CNN FOR TEXT CLASSIFICATION IN TENSORFLOW](http://www.wildml.com/2015/12/implementing-a-cnn-for-text-classification-in-tensorflow/)
8. [Keras predict sentiment-movie-reviews using deep learning](http://machinelearningmastery.com/predict-sentiment-movie-reviews-using-deep-learning/)
9. [Keras sequence-classification-lstm-recurrent-neural-networks](http://machinelearningmastery.com/sequence-classification-lstm-recurrent-neural-networks-python-keras/)
10. [tf-idf + t-sne](https://github.com/lazyprogrammer/machine_learning_examples/blob/master/nlp_class2/tfidf_tsne.py)
11. [Implementation of CNN in sequence classification](https://github.com/dennybritz/cnn-text-classification-tf)
12. [Getting Started with Word2Vec and GloVe in Python](http://textminingonline.com/getting-started-with-word2vec-and-glove-in-python)
13. [PyTorch Implementation of Kim's Convolutional Neural Networks for Sentence Classification](https://github.com/Shawn1993/cnn-text-classification-pytorch)
