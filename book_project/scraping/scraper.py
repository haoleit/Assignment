import json
import os
import re
import time
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/"
CATEGORY = "default"
OUTPUT_FILE = "books.json"
HTML_BACKUP_DIR = "html_backup"
NUM_PAGES = 3

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

STAR_MAPPING = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}


def get_category_url(category):
    res = requests.get(BASE_URL, headers=HEADERS)
    soup = BeautifulSoup(res.text, "html.parser")
    for link in soup.select(".nav-list ul li a"):
        if category.lower() in link.text.strip().lower():
            return BASE_URL + link['href']
    raise ValueError(f"Category '{category}' not found")


def extract_book_info(book, base_url):
    title = book.h3.a['title']
    product_url = base_url + book.h3.a['href'].replace('../../../', 'catalogue/')
    price_str = book.select_one(".price_color").text.strip()
    price_cleaned = re.sub(r'[^\d\.]', '', price_str)  # Chỉ giữ số và dấu chấm
    price = float(price_cleaned)
    availability = book.select_one(".availability").text.strip()
    star_class = book.select_one("p.star-rating")['class'][1]
    rating = STAR_MAPPING.get(star_class, 0)

    # Save HTML backup
    response = requests.get(product_url, headers=HEADERS)
    
    if response.status_code == 200:
        filename = os.path.join(HTML_BACKUP_DIR, f"{title.replace('/', '_').replace(':','')}.html")
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(response.text)

    return {
        "title": title,
        "price": price,
        "availability": availability,
        "product_page": product_url,
        "star_rating": rating
    }


def scrape_books():
    os.makedirs(HTML_BACKUP_DIR, exist_ok=True)

    category_url = get_category_url(CATEGORY)
    scraped_books = []

    for page in range(1, NUM_PAGES + 1):
        if page == 1:
            url = category_url
        else:
            url = category_url.replace("index.html", f"page-{page}.html")
        print(f"Scraping {url}")
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.select(".product_pod")
        for book in books:
            try:
                book_info = extract_book_info(book, BASE_URL)
                scraped_books.append(book_info)
                time.sleep(1)  # polite crawling
            except Exception as e:
                print(f"Error: {e}")
                continue

    # Save to CSV
   # Save to JSON
    with open(OUTPUT_FILE, mode="w", encoding='utf-8') as f:
        json.dump(scraped_books, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Scraping completed. {len(scraped_books)} books saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    scrape_books()

  