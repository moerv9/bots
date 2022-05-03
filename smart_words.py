# Bot to get smarter with learning new words

#imports
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup


class SmartWords():

    def __init__(self):
    #BeautifulSoup Setup
        page = urlopen('https://www.der-karriereguru.de/blog/intelligenter-wirken-mit-diesen-50-fremdwortern')
        html_bytes = page.read()
        html = html_bytes.decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')

        #Search for words
        div = soup.find(class_="w-richtext")
        self.data = []

        for p in div.find_all('p')[5:]:
            self.data.append(p)
            
        self.random_word = np.random.choice(self.data)
            
    def get_new_random_word(self):
        self.random_word = np.random.choice(self.data)
        return self.random_word



