# web_scraper_main.py - Python Data Web Scraper

import requests
from bs4 import BeautifulSoup

def scrape_data(url):
    """Mengambil dan mengurai data dari URL yang diberikan."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() 
        
        soup = BeautifulSoup(response.text, 'html.parser')
        # Contoh: Mengambil semua tautan dari halaman
        links = [a['href'] for a in soup.find_all('a', href=True)]
        
        print(f"Berhasil mengambil {len(links)} tautan dari {url}")
        return links
        
    except requests.exceptions.RequestException as e:
        print(f"Error saat mengambil data: {e}")
        return []

if __name__ == "__main__":
    target_url = "https://www.example.com" # Ganti dengan URL yang ingin di-scrape
    data_links = scrape_data(target_url)
    if data_links:
        print("Scraper berjalan sukses.")
    else:
        print("Scraper gagal dijalankan atau tidak menemukan data.")
