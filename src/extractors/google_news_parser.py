thonfrom bs4 import BeautifulSoup

def parse_article(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    articles = []

    for item in soup.find_all('div', {'class': 'xrnccd'}):
        title = item.find('a', {'class': 'DY5T1d'}).get_text()
        link = "https://news.google.com" + item.find('a', {'class': 'DY5T1d'})['href']
        source = item.find('div', {'class': 'SVJrMe'}).get_text()
        published_at = item.find('time')['datetime']
        image = item.find('img')['src'] if item.find('img') else None

        article = {
            'title': title,
            'link': link,
            'source': source,
            'publishedAt': published_at,
            'image': image
        }
        articles.append(article)

    return articles