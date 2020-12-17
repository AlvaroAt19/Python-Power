# -*- coding: utf-8 -*-
"""
@author: Alvaro
"""

import requests
import time
import webbrowser
import pprint

#The hackernews api url that will show the top 500 news
url_top_500 = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'

#Requesting the page and selecting the top 10 news
r = requests.get(url_top_500)
top_10 = r.json()[:10]

#Url from api to get the top 10 :title and url
url_api = 'https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'
top_10_urls = []

#Making the program pretty
print('-'*70)
print('-'*20 +'Now the top 10 from hackernews' + '-'*20)
time.sleep(5)

#Title and url for the top 10 news
for new in top_10:
    r = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{new}.json?print=pretty')
    pprint.pprint(r.json()['title'])
    top_10_urls.append(r.json()['url'])
    time.sleep(1)

#Function to choose news
def news_check():
    while True:
        try:
            print('Choose news from 1 to 10')
            resp = input('Only numbers(press q to quit): ')
            if resp.lower() == 'q':
                break
            resp = int(resp)
            assert resp > 0 and resp < 11
        except:
            print('You made a mistake, try again')
        else:
            url = top_10_urls[resp-1]
            #Using webbrowser to open the url
            webbrowser.open_new(url)
            break

#Looping to open the selected news
while True:
    again = input('Do you wanna check news?Y/N: ')
    if again.lower() == 'y':
        news_check()
    elif again.lower() == 'n':
        print('Thanks for using! Have a nice day')
        break
    else:
        print('You made a mistake, try again')

        