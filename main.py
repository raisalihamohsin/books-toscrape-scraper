import requests
from bs4 import BeautifulSoup
import csv

def scrape_books():
    base_url = "http://books.toscrape.com/catalogue/page-{}.html"
    all_books = []
    page = 1
    
    while True:
        url = base_url.format(page)
        response = requests.get(url)
        
        # Agar page exist nahi karta (404 error) toh loop tod do
        if response.status_code != 200:
            break
            
        soup = BeautifulSoup(response.text, 'html.parser')
        books = soup.find_all('article', class_='product_pod')
        
        # Agar page par koi book nahi hai toh loop tod do
        if not books:
            break
            
        print(f"📄 Scraping Page {page}...")
        
        for book in books:
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text
            all_books.append([title, price])
            print(f"  → {title} - {price}")
        
        page += 1
    
    # ---------- CSV mein save ----------
    with open('all_books.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Price'])
        writer.writerows(all_books)
    
    print(f"\n✅ Total {len(all_books)} books scraped and saved to all_books.csv")

if __name__ == "__main__":
    scrape_books()