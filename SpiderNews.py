import requests
from bs4 import BeautifulSoup
import html2text
import time


class SpiderNews:
    """
    USAGE:
        1. construct a spider
        url       = "https://www.businesswire.com/..."
        word_list = ["Apple", "yahoo",..]

        spider    = SpiderNews(url, word_list)

        2. use methods as needed
        status    = spider.get_status()
        text      = spider.get_text()
        words     = spider.get_words()
        key_words = spider.search_words()

        OR

        spider_status = SpiderNews(url, word_list).get_status()
    """
    ###########################
    #
    #############INIT##############
    def __init__(self, url, word_list):
        self.url = url
        self.word_list = word_list
    ###########################
    #
    ###########GET STATUS################
    def get_status(self):
        """
        Check if request was successfull
        If not wait 10 seconds and retry 
        """
        try:
            return requests.get(self.url).status_code == 200
        except:
            time.sleep(10)
            try:
                return requests.get(self.url).status_code == 200
            except:
                return False
    ###########################
    #
    ###########GET TEXT################
    def get_text(self):
        """
        Takes the url and returns all the text on that site.
        If website can not be reached it will return nothing.
        """
        if SpiderNews.get_status(self):
            response = requests.get(self.url)
            html = BeautifulSoup(response.text, 'html.parser')
            text = html2text.html2text(str(html))
            return text
        else:
            return " "
    ###########################
    #
    ###########GET WORDS################
    def get_words(self):
        """
        counts words in text and returns
        the words in a dict: 
            {'Business': 8, 'Wire': 6,...}
        """ 
        text = SpiderNews.get_text(self) + " "
        words = {}
        word = ""

        for line in text:
            for char in line:
                if char.isalpha():
                    word = word + char
                elif word != "":
                    if word in words:
                        words[word] += 1
                    else:
                        words[word] = 1
                    word = ""
        return words
    ###########################
    #
    ############SEARCH WORDS###############
    def search_words(self):
        """
        Searches words in word_list and
        returns them in a dict:
            {'Business': 8, 'Wire': 6,...}
        """
        words = SpiderNews.get_words(self)
        key_words = {}

        for word in self.word_list:
            if word in words:
                key_words[word] = words[word]

        return key_words
