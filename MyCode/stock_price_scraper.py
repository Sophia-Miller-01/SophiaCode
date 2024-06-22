# stock_price_scraper.py
import requests
from bs4 import BeautifulSoup

def fetch_stock_price(symbol):
    url = f'https://finance.yahoo.com/quote/{symbol}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def parse_stock_price(html):
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.find('fin-streamer', {'data-field': 'regularMarketPrice'}).get_text()
    return price

if __name__ == "__main__":
    stock_symbol = 'AAPL'
    html = fetch_stock_price(stock_symbol)
    if html:
        stock_price = parse_stock_price(html)
        print(f"Stock price for {stock_symbol}: {stock_price}")
    else:
        print("Failed to retrieve stock price")
