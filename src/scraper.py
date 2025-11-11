thonimport requests
from datetime import datetime
from .extractors.google_news_parser import parse_article
from .extractors.utils_date import format_date

def fetch_articles(query, start_date, end_date, max_articles=500):
    url = f"https://news.google.com/search?q={query}&hl=en-US&gl=US&ceid=US:en"
    articles = []
    page = 1

    while len(articles) < max_articles:
        response = requests.get(f"{url}&start={page*10}")
        if response.status_code != 200:
            print(f"Error fetching page {page}: {response.status_code}")
            break

        page_articles = parse_article(response.text)
        for article in page_articles:
            published_date = format_date(article['publishedAt'])
            if start_date <= published_date <= end_date:
                articles.append(article)

        page += 1

    return articles