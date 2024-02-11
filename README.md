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

## Key Functions
- "grab_Krebs_articles" and "grab_hacker_news_articles": These functions fetch the content of the respective websites.
- "parse_Krebs_articles" and "parse_hacker_news_articles": These functions extract relevant information from the fetched content, such as titles, URLs, summaries, and tags.
- "store_Krebs_articles" and "store_hacker_news_articles": These functions store the extracted article data in the database.
- "search_Krebs_articles" and "search_hacker_news_articles": These functions allow you to search for articles based on keywords in the title, summary, or tags.
