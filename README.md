# InfoSec-Article-Crawler
 Inspired by my time as an Analyst creating weekly security newsletters, this Python script automates the process of fetching, parsing, and storing cybersecurity articles from the popular security website KrebsOnSecurity.com

## Features

- Fetch articles from krebsonsecurity.com.
- Parse articles using BeautifulSoup for web scraping.
- Store articles in a SQLite database for easy retrieval and search.
- Search for articles based on specific keywords.
- Secure coding practices implemented for robustness and security.

## Requirements

- Python 3.8 or higher
- BeautifulSoup
- Requests

## Function
- main.py is the main script that orchestrates the process of collecting and storing articles. It first defines the URLs of the two websites. Then, it calls functions from article_script.py to grab the content of each website, parse the content to extract the articles, and store the articles in a SQLite database named articles.db. Finally, it searches for articles in the database that contain specific keywords and prints the results.
- article_script.py contains functions that are used to grab, parse, and store articles. It has separate functions for handling articles from Krebs on Security and Hacker News, as the websites have different HTML structures. The functions for grabbing the content of the websites use the requests and urllib libraries, and the functions for parsing the content use the BeautifulSoup library.

