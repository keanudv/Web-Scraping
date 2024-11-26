# Import the libraries
import requests
from bs4 import BeautifulSoup

# Defines a function, called scrape_data(), to gather product name and price data
def scrape_data(url, name_tag, name_class, price_tag, price_class):
    '''
    This function scrapes product name and price data from a given website.

    Parameters:
    1. url - The target webpage URL.
    2. name_tag - The HTML tag for the product name.
    3. name_class - The HTML class for the product name.
    4. price_tag - The HTML tag for the product price.
    5. price_class - The HTML class for the product price.

    Returns:
    Show the name and price of each product on the webpage.
    '''

    # Creates a variable, called headers, to store my user-agent string
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"}
    '''
    This is needed because website may block requests that do not come from a legitimate user's browser. By changing the headers to include a user-agent string, we can bypass this restrictions.
    '''

    # Creates a variable, called response, to store the results of the HTTP GET request
    response = requests.get(url, headers=headers)

    # Checks if the request was successful (200 status code)
    if response.status_code == 200:

        # If successful, parse the content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Creates an empty list to store the data
        products = []

        # Loops through each product on the webpage to extract the name and price data
        for product in soup.find_all(name_tag, class_=name_class):

            # Extracts the product name
            name = product.contents[0].strip() if product else "Name Not Found"

            # Extracts the product price
            price_element = product.find_next(price_tag, class_=price_class)
            price = price_element.text.strip() if price_element else "Price Not Found"

            # Adds the data to the empty list
            products.append(
                {
                    "name": name,
                    "price": price
                }
            )

        # Prints out the product names and price data
        for i, product in enumerate(products, 1):
            print(f"{i}. {product['name']} - {product['price']}")

    # If not successful, show the error message
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Foodland example: Scrapes the Product Name and Price per Pound Data
if __name__ == "__main__":
    scrape_data(
        url="https://shop.foodland.com/sm/planning/rsid/11/categories/fruits-vegetables/fresh-fruits-id-47", 
        name_tag="div", 
        name_class="ProductCardstyles__DivKeyboardHandled-sc-fhu8gl-0 cjvWLW", 
        price_tag="span",
        price_class="ProductCardPriceInfo--18y10ci bWqNFy"
    )
