from bs4 import BeautifulSoup

def parse_news_html(html_content: str) -> list:
    soup = BeautifulSoup(html_content, 'html.parser')
    articles = []

    # Find all list items which seem to contain articles
    list_items = soup.find_all("li", class_="ssrcss-rs7w2i-ListItem")

    for li in list_items:
        # Find the link and title within the list item
        link_tag = li.find("a", class_="ssrcss-afqep1-PromoLink")
        title_tag = li.find("p", class_="ssrcss-17zglt8-PromoHeadline")
        summary_tag = li.find("p", class_="ssrcss-1q0x1qg-Paragraph")

        if link_tag and title_tag:
            title = title_tag.get_text(strip=True)
            link = "https://www.bbc.co.uk" + link_tag.get('href', '')
            summary = summary_tag.get_text(strip=True) if summary_tag else ''
            
            articles.append({
                "title": title,
                "url": link,
                "summary": summary
            })

    return articles

