import requests
import sqlite3
from bs4 import BeautifulSoup
import urllib.request
import validators 

def grab_Krebs_articles(url):  # grabs the content of desired website(krebs)
    if not validators.url(url): #validating the URL
    	print("Invalid URL provided.")
    	return None
    
    try:
    	response = requests.get(url)
    	response.raise_for_status() 
    	return response.content
    except requests.RequestException as e:
    	print("Error accessing URL:", e)
    	return None

def grab_hacker_news_articles(url):
    if not validators.url(url): #validating the URL
    	print("Invalid URL provided.")
    	return None
    	
    try:
    	with urllib.request.urlopen(url) as response:
    		return response.read()
    except urllib.error.URLError as e:
    	print("Error accessing URL:", e)

def parse_Krebs_articles(content):  # function to extract article elements
    soup = BeautifulSoup(content, "html.parser")
    articles = soup.find_all("article")  # looks and finds elements w/ "article" tag
    return articles

def parse_hacker_news_article(content):
    soup = BeautifulSoup(content, "html.parser")
    articles = soup.find_all("div", class_="body-post clear")
    parsed_articles = []
    
    # Iterate over each article found
    for article in articles:
        
        title_element = article.find("h2", class_="home-title")
        title = title_element.text.strip() if title_element else "No title found"
        
        date_element = article.find("span", class_="meta-date")
        date = date_element.text.strip() if date_element else "No date found"
        
        article_url = article.find('a')['href']
                
        # Creating a dictionary representing the parsed article
        parsed_article = {
            "title": title,
            "date": date,
            "url": article_url
        }
        
        # Appending the parsed article dictionary
        parsed_articles.append(parsed_article)
        
    # Return the list of parsed articles
    return parsed_articles

def store_Krebs_articles(articles, conn):  # stores extracted articles to a database
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS articles")
    cursor.execute("""CREATE TABLE IF NOT EXISTS articles(
        title TEXT,
        url TEXT,
        summary TEXT,
        tags TEXT,
        date TEXT)""")

    for article in articles:
        title = article.find("h2", class_="entry-title")
        if title:
            article_url = title.find("a")["href"]
            summary_element = article.find_all("div", class_="entry-summary")
            if summary_element:
                summary = summary_element[0].find("p").text
            else:
                summary = "No summary found."

            tags_element = article.find("div", class_="tags")
            if tags_element:
                tags = [tag.text for tag in tags_element.find_all("a")]
            else:
                tags = []
            date_element = article.find("span", class_="date updated")

            cursor.execute("INSERT INTO articles (title, url, summary, tags, date) VALUES (?,?,?,?,?)",
                           (title.text.strip(), article_url, summary.strip(), ",".join(tags), date_element.text.strip()))
            conn.commit()

def store_hacker_news_articles(articles, conn):
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS hacker_news_articles(""title TEXT,""url TEXT)")

    for article in articles:
        title = article['title']
        url = article['url']
        cursor.execute("INSERT INTO hacker_news_articles (title,url) VALUES (?,?)", (title, url))
        conn.commit()

def search_Krebs_articles(conn, keyword):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM articles WHERE LOWER(title) LIKE ? OR LOWER(summary) LIKE ? OR LOWER(tags) LIKE ?",
                   ('%' + keyword.lower() + '%', '%' + keyword.lower() + '%', '%' + keyword.lower() + '%'))
    results = cursor.fetchall()
    if results:
        print("Articles found containing the keyword:", keyword)
        print("=" * 50)
        for row in results:
            print("Title:", row[0])
            print("URL:", row[1])
            print("Summary:", row[2])
            print("Tags:", row[3].split(','))
            print("Date:", row[4])
            print("-" * 50)
    else:
        print("No articles found matching the keyword:", keyword)

def search_hacker_news_articles(conn, keyword):
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT * FROM hacker_news_articles WHERE LOWER(title) LIKE ?", ('%' + keyword.lower() + '%',))
    results = cursor.fetchall()
    if results:
        print("Hacker News articles found containing the keyword:", keyword)
        print("=" * 50)
        for row in results:
            print("Title:", row[0])
            print("URL:", row[1])
            print("-" * 50)
    else:
        print("No Hacker News articles found matching the keyword:", keyword)
        print("*" * 50)

