import requests
from bs4 import BeautifulSoup

def scrape_links(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True)]
        return links
    except Exception as e:
        return [f'Error: {e}']
