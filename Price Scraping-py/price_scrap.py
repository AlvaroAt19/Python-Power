# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 08:46:02 2021

@author: Alvar
"""
import requests
from bs4 import BeautifulSoup

def find_price(url,selector):
    """Find the price for some product using the url, and the element selector 
    from source code"""
    req = requests.get(url) 
    req.raise_for_status()
    soup = BeautifulSoup(req.text,'html.parser')
    lst = soup.select(selector)
    return lst[0].text.strip()


