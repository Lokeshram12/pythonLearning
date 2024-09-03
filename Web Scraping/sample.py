#  pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup

# Read the HTML content from the file
with open('/workspaces/pythonLearning/Web Scraping/index.html', 'r') as file:
    html_content = file.read()
    print(html_content)
    soup = BeautifulSoup(html_content, 'html.parser')
    print(soup)
    # Get the title of the page
    title = soup.title.text
    print(f"Title of the page: {title}")

    # Find all <h1> tags
    headers = soup.find_all('h1')
    for header in headers:
        print(f"Header: {header.text}")

# Find and print all items in the list under Section 1
    section1 = soup.find(id='section1')
    list_items = section1.find_all('li')
    for item in list_items:
        print(f"List item: {item.text}")

