from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def scrape_books():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def scrape_books():
    driver = webdriver.Chrome()
    driver.get("http://books.toscrape.com")

    books = []

    items = driver.find_elements(By.CLASS_NAME, "product_pod")

    for item in items[:10]:  # limit to 10 books
        title = item.find_element(By.TAG_NAME, "h3").text

        books.append({
            "title": title,
            "author": "Unknown",
            "description": "Sample description",
            "rating": 4.0,
            "url": "http://books.toscrape.com"
        })

    driver.quit()
    return books