import sqlite3
from article_script import grab_Krebs_articles, parse_Krebs_articles, store_Krebs_articles, search_Krebs_articles
from article_script import grab_hacker_news_articles, parse_hacker_news_article, store_hacker_news_articles, search_hacker_news_articles

def main():
    conn = None
    try:
        krebs_url = "https://krebsonsecurity.com/" # specifies URL
        krebs_content = grab_Krebs_articles(krebs_url) # gets website content
        krebs_articles = parse_Krebs_articles(krebs_content) # parses content for extraction
        
        hacker_news_url = "https://thehackernews.com/"
        hacker_news_content = grab_hacker_news_articles(hacker_news_url)
        #print("hacker_news_content:", hacker_news_content)
        hacker_news_articles = parse_hacker_news_article(hacker_news_content)
        
        conn = sqlite3.connect("articles.db")
        store_Krebs_articles(krebs_articles, conn) # store Krebs articles to db
        store_hacker_news_articles(hacker_news_articles, conn) # store hackernews articles to db
        
        # Searching Krebs
        search_Krebs_articles(conn, "Google")
        search_Krebs_articles(conn, "Hacker")
        search_Krebs_articles(conn, "Bitcoin")
        
        # Searching hacker news
        search_hacker_news_articles(conn, "Raspberry")
        search_hacker_news_articles(conn, "OpenAI")
        search_hacker_news_articles(conn, "Android")
        
    except Exception as e:
        print("An error occurred:", e)

    finally:
    	if conn is not None:
    		conn.close()

if __name__ == "__main__":
    main()
