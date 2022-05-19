# -*- coding: utf-8 -*-
"""
Created on Fri May  6 14:43:11 2022

@author: DennisLin
"""

import requests
from bs4 import BeautifulSoup

resp = requests.get('http://jwlin.github.io/py-scraping-analysis-book/ch2/table/table.html')
soup = BeautifulSoup(resp.text, 'html.parser')

prices =[]
rows = soup.find('table', 'table').tbody.find_all('tr')
for row in rows:
    price = row.find_all('td')[2].text
    prices.append(int(price))

print()    
print('Method 1:')
print(sum(prices)/len(prices))
print()
prices.clear()

links = soup.find_all('a')
for link in links:
    price = link.parent.previous_sibling.text
    prices.append(int(price))

print("Method 2:")
print(sum(prices)/len(prices))
print()

for row in rows:
    all_tds = row.find_all('td') #The same as the lint below
    all_tds = [td for td in row.children] #The same as the line above
    if 'href' in all_tds[3].a.attrs:
        href = all_tds[3].a['href']
    else:
        href = None
    print(all_tds[0].text, all_tds[1].text, all_tds[2].text, href, all_tds[3].a.img['src'])
print()

for row in rows:
    print([s for s in row.stripped_strings])
    