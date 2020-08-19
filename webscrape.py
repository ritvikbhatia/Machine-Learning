from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url="https://www.youtube.com/results?search_query=travel";
uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
yt_href=[]
yt_title=[]
page_soup=soup(page_html,"html.parser")
yt_links = page_soup.find_all("a", class_ = "yt-uix-tile-link")
for x in yt_links:
    yt_href.append(x.get("href"))
    yt_title.append(x.get("title"))
print(yt_href)
#containers=page_soup.findAll("div",{"class":"item-container"})
