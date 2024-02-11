import sqlite3
from article_script import grab_articles, parse_articles, store_articles, search_articles

def main():
    try:
        target_url = "https://krebsonsecurity.com/" #specifies url
        articles_content = grab_articles(target_url) #gets website content
        articles = parse_articles(articles_content) #parses content for extraction
        
        conn = sqlite3.connect("articles.db")
        store_articles(articles, conn)
        
        search_articles(conn, "Google")
        search_articles(conn, "Hacker")
        search_articles(conn, "Bitcoin")
        
    except Exception as e:
        print("An error occurred:", e)

    finally:
        conn.close()

if __name__ == "__main__":
    main()
