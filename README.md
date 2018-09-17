# Rotten_tomato_scraper

A python program that only require you to enter the rotten tomato page url you want to scrape data of and it will fetch all the movie link attacted on that page and scrape all the relevant info regarding those movies such as audience score, genre, director ,runtime ,image url etc


## Library used
1. BeautifulSoup
2. Request
3. pandas
4. urllib




## Getting Started

To set up the project in your local enivironment ,first clone the repository and save it on your local environment/machine.
To run the project you need python 3.6 or higher to be installed on your machine, i'll personally recommend Anaconda .
got to the last line in the code mention below and change/enter the the url in crawl().you can enter any rotten tomato page that have movies listed on them like top 100 movie of all time or best horror movies 2018 page .
```
crawl('https://www.rottentomatoes.com/top/bestofrt/top_100_documentary_movies/')
```

