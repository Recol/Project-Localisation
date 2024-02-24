from bs4 import BeautifulSoup

def parse_news_html(html_content: str) -> list:
    soup = BeautifulSoup(html_content, 'html.parser')
    articles = []

    # Find all article containers
    articles_divs = soup.find_all("div", class_="gs-c-promo")

    for article in articles_divs:
        title_tag = article.find("h3", class_="gs-c-promo-heading__title")
        link_tag = article.find("a", class_="gs-c-promo-heading")
        summary_tag = article.find("p", class_="gs-c-promo-summary")

        if title_tag and link_tag and summary_tag:
            title = title_tag.get_text(strip=True)
            link = "https://www.bbc.co.uk" + link_tag.get('href', '')
            summary = summary_tag.get_text(strip=True)

        # New code to extract the image source
        image_tag = article.find("img")
        image_src = image_tag['src'] if image_tag and image_tag.has_attr('src') else ''
        image_src = image_src if image_src.startswith('http') else f"https:{image_src}"

        article_info = {
            "title": title,
            "url": link,
            "summary": summary,
            "image_src": image_src  # Add the image source to the dictionary
        }
        articles.append(article_info)


    return articles
