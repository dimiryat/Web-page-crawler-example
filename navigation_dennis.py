# -*- coding: utf-8 -*-
"""
Created on Fri May  6 14:58:16 2022

@author: DennisLin
"""

import requests
from bs4 import BeautifulSoup

resp = requests.get('http://jwlin.github.io/py-scraping-analysis-book/ch2/table/table.html')
soup = BeautifulSoup(resp.text, 'html.parser')

Total = []

#print('============================================================')
L1 = soup.find('tbody').find_all('tr')
for L2 in L1:
    L3 = L2.find_all('td')[2]
    for L4 in L3:
        print(L4.text)