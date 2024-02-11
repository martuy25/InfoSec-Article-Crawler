import requests #for making HTTP requests
import sqlite3
from bs4 import BeautifulSoup

def grab_articles(url): #grabs the content of desired website
    response = requests.get(url)
    response.raise_for_status()  #error for non-200 status codes
    return response.content

def parse_articles(content): #function to extract article elements
    soup = BeautifulSoup(content, "html.parser")
    articles = soup.find_all("article") #looks and finds elements w/ "article" tag
    return articles

def store_articles(articles, conn): #stores extracted articles to a database
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
                tags =[]
            date_element = article.find("span", class_="date updated")

            cursor.execute("INSERT INTO articles (title, url, summary, tags, date) VALUES (?,?,?,?,?)",
                           (title.text.strip(), article_url, summary.strip(), ",".join(tags), date_element.text.strip()))
            conn.commit()

def search_articles(conn, keyword):
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
