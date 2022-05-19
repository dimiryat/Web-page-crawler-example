# -*- coding: utf-8 -*-
"""
Created on Fri May  6 11:05:07 2022

@author: DennisLin
"""

import requests
from bs4 import BeautifulSoup

resp = requests.get('http://jwlin.github.io/py-scraping-analysis-book/ch2/blog/blog.html')
soup = BeautifulSoup(resp.text, 'html.parser')

print(soup.find('h4'))
print()

print(soup.h4.a.text)
print()

main_titles = soup.find_all("h4")
for title in main_titles:
    print(title.a.text)
print()

main_titles = soup.find_all('h4', {'class':'card-title'})
for title in main_titles:
    print(title.a.text)
print()

print("soup.find(id='mac-p')")
print(soup.find(id='mac-p'))
print()

print(soup.find('', {'data-foo':'mac-foo'}))
print()

divs = soup.find_all('div', 'content')
for div in divs:
    print(div.text)
print()
print("==================================================================")
print()

divs = soup.find_all('div', 'content')
for div in divs:
    print(div.h6.text.strip(), div.h4.a.text.strip(), div.p.text.strip())
print()

divs = soup.find_all('div', 'content')
for div in divs:
    print([s for s in div.stripped_strings])