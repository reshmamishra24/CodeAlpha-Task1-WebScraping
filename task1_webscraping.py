import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com/catalogue/page-1.html"

# Empty list to store data
titles = []
prices = []
ratings = []

# Loop through first 5 pages (you can increase if needed)
for page in range(1, 6):
    page_url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")
    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.p["class"][1]  # Rating is stored in class name
        
        titles.append(title)
        prices.append(price)
        ratings.append(rating)

# Create DataFrame
df = pd.DataFrame({
    "Title": titles,
    "Price": prices,
    "Rating": ratings
})

# Save to CSV
df.to_csv("books_data.csv", index=False)

print("Task 1 Complete! Data saved to books_data.csv")