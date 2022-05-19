# -*- coding: utf-8 -*-
"""
Created on Mon May  9 09:30:29 2022

@author: DennisLin
"""

import requests
from bs4 import BeautifulSoup

resp = requests.get('http://jwlin.github.io/py-scraping-analysis-book/ch2/blog/blog.html')
soup = BeautifulSoup(resp.text, 'html.parser')

import re

for img in soup.find_all('img',{'src':re.compile('beginner.*\.png$')}):
    print(img['src'])