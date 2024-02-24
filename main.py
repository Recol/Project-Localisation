from fastapi import FastAPI
from news_fetcher import fetch_news_content
from news_parser import parse_news_html
import httpx
import logging

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.get("/news/{region}/{city_area}")
def read_news(region: str, city_area: str):
    url = f"https://www.bbc.co.uk/news/{region}/{city_area}"
    try:
        logging.info(f"Fetching news content from URL: {url}")
        html_content = fetch_news_content(url)
        if not html_content:
            logging.warning(f"Received empty content from URL: {url}")
        news_articles = parse_news_html(html_content)
        if not news_articles:
            logging.warning(f"No articles were extracted from the content.")
        return {"url": url, "articles": news_articles}
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error occurred: {e.response.status_code}")
        return {"error": f"HTTP error occurred: {e.response.status_code}"}
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return {"error": f"An error occurred: {str(e)}"}