# InfoSec-Article-Crawler
This directory contains two Python files, main.py and article_script.py, which work together to scrape articles from two websites, Krebs on Security and Hacker News, and store them in a SQLite database.

## Features

- Fetch articles from krebsonsecurity.com and thehackernews.com.
- Parse articles using BeautifulSoup for web scraping.
- Store articles in a SQLite database for easy retrieval and search.
- Search for articles based on specific keywords.
- Secure coding practices implemented for robustness and security.

## Requirements

- Python 3.8 or higher
- BeautifulSoup
- Requests

## Main.py
- main.py is the main script that orchestrates the scraping and storage process. It defines the following functions:

- grab_Krebs_articles: This function retrieves the HTML content of the Krebs on Security website.
- parse_Krebs_articles: This function parses the HTML content of the Krebs on Security website to extract article titles, URLs, summaries, tags, and dates.
- store_Krebs_articles: This function stores the extracted Krebs on Security articles in a database.
- grab_hacker_news_articles: This function retrieves the HTML content of the Hacker News website.
- parse_hacker_news_article: This function parses the HTML content of the Hacker News website to extract article titles and URLs.
- store_hacker_news_articles: This function stores the extracted Hacker News articles in a database.
- search_Krebs_articles: This function searches for articles in the database that contain a given keyword.
- search_hacker_news_articles: This function searches for articles in the database that contain a given keyword.

## article_script.py
- article_script.py contains helper functions that are used by main.py:

- grab_Krebs_articles: This function retrieves the HTML content of a website using the requests library.
- grab_hacker_news_articles: This function retrieves the HTML content of a website using the urllib library.
- parse_Krebs_articles: This function parses HTML content using the BeautifulSoup library.
- parse_hacker_news_article: This function parses HTML content using the BeautifulSoup library.
- store_Krebs_articles: This function creates and executes SQL statements to store articles in a database.
- store_hacker_news_articles: This function creates and executes SQL statements to store articles in a database.
- search_Krebs_articles: This function creates and executes SQL statements to search for articles in a database.
- search_hacker_news_articles: This function creates and executes SQL statements to search for articles in a database.


