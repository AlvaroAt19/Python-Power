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
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    req = requests.get(url, headers=headers) 
    req.raise_for_status()
    soup = BeautifulSoup(req.text,'html.parser')
    lst = soup.select(selector)
    return lst[0].text.strip()

#Test
Magalu_acer = find_price('https://www.magazineluiza.com.br/notebook-acer-aspire-3-a315-23-r0ld-amd-ryzen-5-12gb-1tb-156-windows-10/p/227606500/in/note/?&force=1&seller_id=magazineluiza&&utm_source=google&utm_medium=pla&utm_campaign=&partner_id=58374&gclid=Cj0KCQiA0MD_BRCTARIsADXoopbOR5GMBJa__buwsnB2LUEb6mjLtOdMXFBSY6KNg55R10n8efXm5NQaAsNPEALw_wcB','body > div.wrapper__main > div.wrapper__content.js-wrapper-content > div.wrapper__control > div.wrapper-product__content.wrapper-product__box-prime > div.wrapper-product__informations.js-block-product > div.information-values__product-page > div > div.price-template__cash > div > span.price-template__text')
Submarino_lenovo = find_price('https://www.submarino.com.br/produto/1608469552','#content > div > div > div.GridUI-wcbvwm-0.jjjQOQ.ViewUI-sc-1ijittn-6.iXIDWU > div > section > div > div.product-main-area__ProductMainAreaUI-wc8uq1-0.eAJbgq.ViewUI-sc-1ijittn-6.iXIDWU > div.product-main-area__OfferBox-wc8uq1-3.jnbife.ViewUI-sc-1ijittn-6.iXIDWU > div > div:nth-child(1) > div > div.main-offer__ContainerUI-sc-1d2zph4-1.dqfqTr.ViewUI-sc-1ijittn-6.iXIDWU > div:nth-child(1) > div > span')
Amazon_asus = find_price('https://www.amazon.com.br/M509da-br324t-Notebook-Ryzen-Windows-Cinza/dp/B0856FXH57/ref=sr_1_4?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=Notebook+ryzen&qid=1609589611&sr=8-4','#price_inside_buybox')
print(f'Magalu_acer:{Magalu_acer}')
print(f'Submarino_lenovo:{Submarino_lenovo}')
print(f'Amazon_asus:{Amazon_asus}')
