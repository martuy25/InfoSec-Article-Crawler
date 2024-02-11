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
- main.py is the main script that orchestrates the scraping and storage process. It defines the following functions:

-- grab_Krebs_articles: This function retrieves the HTML content of the Krebs on Security website.
-- parse_Krebs_articles: This function parses the HTML content of the Krebs on Security website to extract article titles, URLs, summaries, tags, and dates.
-- store_Krebs_articles: This function stores the extracted Krebs on Security articles in a database.
-- grab_hacker_news_articles: This function retrieves the HTML content of the Hacker News website.
-- parse_hacker_news_article: This function parses the HTML content of the Hacker News website to extract article titles and URLs.
-- store_hacker_news_articles: This function stores the extracted Hacker News articles in a database.
-- search_Krebs_articles: This function searches for articles in the database that contain a given keyword.
-- search_hacker_news_articles: This function searches for articles in the database that contain a given keyword.
- article_script.py contains functions that are used to grab, parse, and store articles. It has separate functions for handling articles from Krebs on Security and Hacker News, as the websites have different HTML structures. The functions for grabbing the content of the websites use the requests and urllib libraries, and the functions for parsing the content use the BeautifulSoup library.

