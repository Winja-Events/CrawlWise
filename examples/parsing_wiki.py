import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract the title of the Wikipedia page
        title = soup.select_one('h1').text
        print(f"Title: {title}")

        # Extract the main content of the Wikipedia page
        main_content = soup.select_one('.mw-parser-output').get_text()
        print(f"Main Content:\n{main_content}")

    else:
        print(f"Failed to access the Wikipedia page. Status code: {response.status_code}")

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Web_scraping"  # Replace with the URL of the Wikipedia page you want to scrape
    scrape_wikipedia(url)

