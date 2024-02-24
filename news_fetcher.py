from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time

def fetch_news_content(url: str) -> str:
    # Set up Chrome options for headless browsing
    options = ChromeOptions()
    options.headless = True
    options.add_argument("--disable-gpu")  # This option is necessary for headless mode, even though it's not used.
    options.add_argument("--no-sandbox")  # This option is required if running as root/administrator.
    options.add_argument("--disable-dev-shm-usage")  # Overcomes limited resource problems.

    # Initialize the WebDriver
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)
        # Wait for JavaScript to render the page
        time.sleep(5)  # This is a simplistic way to wait for content to load, consider using WebDriverWait for better reliability.
        html_content = driver.page_source
    finally:
        driver.quit()

    return html_content
