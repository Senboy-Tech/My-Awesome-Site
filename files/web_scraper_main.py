# web_scraper_main.py

import requests
from bs4 import BeautifulSoup

def scrape_data(url):
    """Fungsi sederhana untuk mengambil data dari URL."""
    try:
        response = requests.get(url)
        response.raise_for_status() # Cek error HTTP
        
        soup = BeautifulSoup(response.text, 'html.parser')
        # Temukan semua paragraf
        paragraphs = soup.find_all('p')
        return [p.get_text() for p in paragraphs]
        
    except requests.exceptions.RequestException as e:
        print(f"Error saat mengambil data: {e}")
        return []

if __name__ == "__main__":
    print("Script Web Scraper berhasil dimuat.")
    # data = scrape_data("https://example.com") 
    # print(f"Jumlah paragraf yang ditemukan: {len(data)}")
