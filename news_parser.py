from bs4 import BeautifulSoup

def parse_news_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    articles = []

    # Find the main grid containing the articles using the class name provided
    main_grid = soup.find("ul", class_="ssrcss-1sx4aei-Grid")

    # If the main grid is found, iterate through each list item that represents an article
    if main_grid:
        list_items = main_grid.find_all("li", recursive=False)  # Only direct children

        for item in list_items:
            # Attempt to extract the title, link, and summary for each article
            link_tag = item.find("a", href=True)
            title_tag = item.find("p", class_="ssrcss-17zglt8-PromoHeadline")
            summary_tag = item.find("p", class_="ssrcss-1q0x1qg-Paragraph")

            # If a link and a title are present, extract the text and href
            if link_tag and title_tag:
                title = title_tag.get_text(strip=True)
                link = link_tag['href']
                # Ensure link is absolute
                link = f"https://www.bbc.co.uk{link}" if not link.startswith('http') else link
                summary = summary_tag.get_text(strip=True) if summary_tag else ''

                # Append the article information to the articles list
                articles.append({
                    "title": title,
                    "url": link,
                    "summary": summary
                })

    return articles