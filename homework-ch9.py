from bs4 import BeautifulSoup
import requests
from time import sleep
import re
import matplotlib.pyplot as plt
from collections import Counter


def book_info(td):
 """given a BeautifulSoup <td> Tag representing a book,
 extract the book's details and return a dict"""
 title = td.find("div", "thumbheader").a.text
 by_author = td.find('div', 'AuthorName').text
 authors = [x.strip() for x in re.sub("^By ", "", by_author).split(",")]
 isbn_link = td.find("div", "thumbheader").a.get("href")
 isbn = re.match("/product/(.*)\.do", isbn_link).groups()[0]
 date = td.find("span", "directorydate").text.strip()
 return {
 "title" : title,
 "authors" : authors,
 "isbn" : isbn,
 "date" : date
 }


base_url = "http://www.gu-global.com/tw/store/feature/gu/women/limited/"
books = []

soup = BeautifulSoup(requests.get(base_url ).text, 'html5lib')
for td in soup('div', class_ = "unit"):
    #print td
    date = td.find("dd", "price").text.strip()
    print date

 # now be a good citizen and respect the robots.txt!
