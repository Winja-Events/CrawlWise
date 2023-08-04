iimport requests
from bs4 import BeautifulSoup

def scrape_with_beautifulsoup(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Example: titles = soup.select('h2.title')
        # Example: prices = soup.select('.price')
    else:
        print(f"Failed to access the webpage. Status code: {response.status_code}")

if __name__ == "__main__":
    url = "https://evil.com"  # Replace with the URL of the website you want to scrape
    scrape_with_beautifulsoup(url)

