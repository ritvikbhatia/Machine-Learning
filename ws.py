import csv
import re
import requests
import time
from bs4 import BeautifulSoup

# scrapes the title
def getTitle():
    d = soup.find_all("h1", "branded-page-header-title")
    for i in d:
        name = i.text.strip().replace('\n',' ').replace(',','').encode("utf-8")
        #f.write(name+',')
        print(name)

# scrapes the subscriber and view count
def getStats():
    b = soup.find_all("li", "about-stat ") # trailing space is required.
    for i in b:
        value = i.b.text.strip().replace(',','')
        name = i.b.next_sibling.strip().replace(',','')
        #f.write(value+',')
        #print('\t\t%s = %s') % (name, value)

# scrapes the description
def getDescription():
    c = soup.find_all("div", "about-description")
    for i in c:
        description = i.text.strip().replace('\n',' ').replace(',','').encode("utf-8")
        #f.write(description+',')
        #print('\t\t%s') % (description)

# scrapes all the external links
def getLinks():
    a = soup.find_all("a", "about-channel-link ") # trailing space is required.
    for i in a:
        url = i.get('href')
        #f.write(url+',')
        #print('\t\t%s') % (url)

# scrapes the related channels
def getRelated():
    s = soup.find_all("h3", "yt-lockup-title")
    for i in s:
        t = i.find_all(href=re.compile("user"))
        for i in t:
            url = 'https://www.youtube.com'+i.get('href')
            rCSV.write(url+'\n')
            print(i.text, url)

f = open("youtube-scrape-data.csv", "w+")
rCSV = open("related-channels.csv", "w+")
visited = []
base = "https://www.youtube.com/results?search_query="
q = ['search+query+here']
page = "&page="
count = 1
pagesToScrape = 20

for query in q:
    while count <= pagesToScrape:
        scrapeURL = base + str(query) + page + str(count)
        print('Scraping \n')
        r = requests.get(scrapeURL)
        soup = BeautifulSoup(r.text)
        users = soup.find_all("div", "yt-lockup-byline")
        for each in users:
            a = each.find_all(href=re.compile("user"))
            for i in a:
                url = 'https://www.youtube.com'+i.get('href')+'/about'
                if url in visited:
                    print('\t has already been scraped\n\n')
                else:
                    r = requests.get(url)
                    soup = BeautifulSoup(r.text)
                    f.write(url+',')
                    print(url)
                    getTitle()
                    getStats()
                    getDescription()
                    getLinks()
                    getRelated()
                    f.write('\n')
                    print('\n')
                    visited.append(url)
                    time.sleep(3)
        count += 1
        time.sleep(3)
        print('\n')
    count = 1
    print('\n')
f.close()
