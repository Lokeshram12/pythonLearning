import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'http://books.toscrape.com'

# Send a GET request to the website
response = requests.get(url)

# print(response)
# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    # print(response.content)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all book containers
    books = soup.find_all('article', class_='product_pod')

    # Iterate through each book and extract details
    for book in books:
        # Extract the book title
        title = book.h3.a['title']
        
        # Extract the book price
        price = book.select_one('p.price_color').text
        
        print(f"Title: {title}, Price: {price}")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
