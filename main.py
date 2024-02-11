import sqlite3
from article_script import fetch_articles, parse_articles, store_articles, search_articles

def main():
    try:
        target_url = "https://krebsonsecurity.com/"
        articles_content = fetch_articles(target_url)
        articles = parse_articles(articles_content)
        
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
