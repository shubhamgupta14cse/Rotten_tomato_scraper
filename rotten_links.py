import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import urljoin
import pandas as pd


table=[]
target_url="https://www.rottentomatoes.com"
target_links=[]
#get the main oage
def request(url):
    try:
        r=requests.get(url)
        return r.content

    except:
        print('request error')
        pass

#extract links
def extract_movie_links(url):
    r=request(url)
    list=[]
    try:
        soup=BeautifulSoup(r ,  "html.parser")
        link_list= soup.find_all('a',{'class' :'unstyled articleLink'})
        for link in link_list:
            if "/m/" in str(link):
                link=link['href']
                link=urljoin('https://www.rottentomatoes.com',link)
                list.append(link)
        return list[0:19]
    except:
        print('extract error')
#extract_movie_links('https://www.rottentomatoes.com/top/bestofrt/')
#go to link and collect data
def scrape_data(url):

    r=request(url)
    try:

        soup=BeautifulSoup(r ,  "html.parser")
        movie_title=soup.find('h1',{'data-type' :'title'}).text
        movie_title = ''.join(movie_title.split())
        print(movie_title)
        tomatometer=int(soup.find('div',{'class':'critic-score'}).contents[1].contents[3].contents[0].text)
        print(tomatometer)
        audience_score=int(soup.find('div',{'class':'meter-value'}).contents[1].text.split('%')[0])
        print(audience_score)
        director=soup.find('ul',{'class' :'content-meta info'}).contents[5].contents[3].contents[1].text
        print(director)
        genre=soup.find('ul',{'class' :'content-meta info'}).contents[3].contents[3].contents[1].text
        genre = ''.join(genre.split())
        print(genre)
        try:
            runtime=soup.find('ul',{'class' :'content-meta info'}).contents[13].contents[3].contents[1].text
            runtime = int(''.join(runtime.split()).split('minutes')[0])
            print(runtime)
        except:
            try:
                runtime=soup.find('ul',{'class' :'content-meta info'}).contents[15].contents[3].contents[1].text
                runtime = int(''.join(runtime.split()).split('minutes')[0])
                print(runtime)
            except:
                runtime="none"

        try:
            poster_url= soup.find('img',{'class' :'posterImage'})['src']
            print(poster_url)
        except:
            poster_url='none'
        try:
            background_url=soup.find('div', {'class':'heroImage movie'})['style'].split("url('")[1].split("'")[0]
            print(background_url)
        except:
            try:
                background_url=soup.find('div', {'class':'heroImage movie noCursor'})['style'].split("url('")[1].split("'")[0]
                print(background_url)

            except:
                background_url="none"





        #create dictonary
        data={'title':movie_title,
        'tomatometer':tomatometer,
        'audience_score':audience_score,
        'director':director,
        'genre':genre,
        'runtime':runtime,
        'poster_url':poster_url,
        'background_url':background_url}
        #print(data)
        return data
    except:
        pass

def crawl(url):


    #get all movie links on page
    link_list=extract_movie_links(url)

    #scrape data for that movie
    for link in link_list:
        #print(link)
        data=scrape_data(link)
        table.append(data)

crawl('https://www.rottentomatoes.com/top/bestofrt/top_100_documentary_movies/')

print(pd.DataFrame(table))




#crawl('https://www.rottentomatoes.com/top/bestofrt/top_100_documentary_movies/')
#scrape_data("https://www.rottentomatoes.com/m/the_wizard_of_oz_1939")
#print(scrape_data('https://www.rottentomatoes.com/m/the_last_waltz_1978'))
