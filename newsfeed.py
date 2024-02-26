import feedparser
import random
import time

def GetArticles():
        
    # List of RSS feed URLs
    rss_urls = ['https://www.polygon.com/rss/index.xml', 'https://www.theverge.com/rss/index.xml', 'https://www.gamespot.com/feeds/game-news/', 'https://www.vox.com/rss/index.xml', 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml']

    # Initialize an empty list to hold the posts from all feeds
    all_posts = []

    # Loop over each URL
    for url in rss_urls:
        # Parse the feed
        feed = feedparser.parse(url)
        
        # Loop over each post in the feed
        for post in feed.entries:
            # Add the post to the all_posts list
            all_posts.append(post)
            print(post.title)

    return all_posts

GetArticles()
