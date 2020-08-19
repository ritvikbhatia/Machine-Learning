from bs4 import BeautifulSoup
import requests
import csv
csv_file = open('YouTube scraping.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Video Id','Title', 'Description','Category'])
count=1

while count <= 40:


    source = requests.get("https://www.youtube.com/results?search_query=travel&page="+str(count)).text
    soup = BeautifulSoup(source, 'html.parser')
    count=count+1;


    for content in soup.find_all('div', class_= "yt-lockup-content"):
        try:
            title = content.h3.a.text.encode()
            print(title)

            description = content.find('div', class_="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2").text
            print(description)

            ref=content.h3.a['href']
            d=ref.split('=')[1]
            print(d)

        except Exception as e:
            description = None
            d=None
            tit=None


        print('\n')
        csv_writer.writerow([d,title,description,'travel'])

count=1
while count <= 40:


    source = requests.get("https://www.youtube.com/results?search_query=food&page="+str(count)).text
    soup = BeautifulSoup(source, 'html.parser')
    count=count+1;


    for content in soup.find_all('div', class_= "yt-lockup-content"):
        try:
            title = content.h3.a.text.encode()
            print(title)

            description = content.find('div', class_="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2").text
            print(description)

            ref=content.h3.a['href']
            d=ref.split('=')[1]
            print(d)

        except Exception as e:
            description = None
            d=None
            tit=None


        print('\n')
        csv_writer.writerow([d,title,description,'food'])

count=1
while count <= 40:


    source = requests.get("https://www.youtube.com/results?search_query=science&page="+str(count)).text
    soup = BeautifulSoup(source, 'html.parser')
    count=count+1;


    for content in soup.find_all('div', class_= "yt-lockup-content"):
        try:
            title = content.h3.a.text.encode()
            print(title)

            description = content.find('div', class_="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2").text
            print(description)

            ref=content.h3.a['href']
            d=ref.split('=')[1]
            print(d)

        except Exception as e:
            description = None
            d=None
            tit=None


        print('\n')
        csv_writer.writerow([d,title,description,'science'])


count=1
while count <= 40:


    source = requests.get("https://www.youtube.com/results?search_query=Manufacturing&page="+str(count)).text
    soup = BeautifulSoup(source, 'html.parser')
    count=count+1;


    for content in soup.find_all('div', class_= "yt-lockup-content"):
        try:
            title = content.h3.a.text.encode()
            print(title)

            description = content.find('div', class_="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2").text
            print(description)

            ref=content.h3.a['href']
            d=ref.split('=')[1]
            print(d)

        except Exception as e:
            description = None
            d=None
            tit=None


        print('\n')
        csv_writer.writerow([d,title,description,'Manufacturing'])
count=1
while count <= 40:


    source = requests.get("https://www.youtube.com/results?search_query=History&page="+str(count)).text
    soup = BeautifulSoup(source, 'html.parser')
    count=count+1;


    for content in soup.find_all('div', class_= "yt-lockup-content"):
        try:
            title = content.h3.a.text.encode()
            print(title)

            description = content.find('div', class_="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2").text
            print(description)

            ref=content.h3.a['href']
            d=ref.split('=')[1]
            print(d)

        except Exception as e:
            description = None
            d=None
            tit=None


        print('\n')
        csv_writer.writerow([d,title,description,'History'])
count=1
while count <= 40:


    source = requests.get("https://www.youtube.com/results?search_query=Art&page="+str(count)).text
    soup = BeautifulSoup(source, 'html.parser')
    count=count+1;


    for content in soup.find_all('div', class_= "yt-lockup-content"):
        try:
            title = content.h3.a.text.encode()
            print(title)

            description = content.find('div', class_="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2").text
            print(description)

            ref=content.h3.a['href']
            d=ref.split('=')[1]
            print(d)

        except Exception as e:
            description = None
            d=None
            tit=None


        print('\n')
        csv_writer.writerow([d,title,description,'Art and Music'])
csv_file.close()
