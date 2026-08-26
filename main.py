import requests
from bs4 import BeautifulSoup

# 1. Website se data lao
url = "http://books.toscrape.com/"
response = requests.get(url)

# 2. Check karo ke site ne access diya ya nahi
if response.status_code == 200:
    print("Website connected successfully!")
    
    # 3. HTML ko parse karo (BeautifulSoup samajh leta hai)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 4. Saari books dhundho (HTML mein <article> tag hai)
    all_books = soup.find_all('article', class_='product_pod')
    
    # 5. Har book ka data print karo
    for book in all_books:
        # Title nikaalo
        title = book.h3.a['title']  # <h3> ke andar <a> ki 'title' attribute
        
        # Price nikaalo
        price = book.find('p', class_='price_color').text  # <p> tag ka text
        
        print(f"Title: {title} | Price: {price}")
        
else:
    print(f"Site ne access nahi diya. Status code: {response.status_code}")