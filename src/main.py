import requests
from bs4 import BeautifulSoup
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

url = 'https://www.google.com/search?q=bitcoin+price+to+dollar'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def get_bitcoin_price():
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad HTTP status
        soup = BeautifulSoup(response.text, 'html.parser')

        # Try to find the price element
        price_element = soup.find('span', class_='pclqee')
        if price_element:
            price = price_element.text
        else:
            price = 'Price element not found'

    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
        price = 'Error: Unable to retrieve price'
    except Exception as err:
        logging.error(f"An error occurred: {err}")
        price = 'Error: Something went wrong'

    return price

# Adding delay to prevent being flagged
time.sleep(2)

# Get and print Bitcoin price
bitcoin_price = get_bitcoin_price()
print(f'The Bitcoin Price: {bitcoin_price}')