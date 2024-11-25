# Import the libraries
import requests
from bs4 import BeautifulSoup

# Defines a function, called scrape_data(), to gather product name and price data
def scrape_data(url, name_tag, name_class, price_tag, price_class):
  '''
  This function scrapes product name and price data from a given website.

  Parameters:
  1. url - The target webpage url.
  2. name_teg - The HTML tag for the product name.
  3. name_class - The HTML class for the product name.
  4. price_tag - The HTML tag for the product price.
  5. price_class - The HTML class foe the product price.

  Returns:
  Show the name and price of each product on the webpage.
  '''

  # Creates a variable, called headers, to store my user-agent string
  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"}
  '''
  This is needed because the website may block requests that do not come from a legitimate user's browser. By changing the headers to include a user-agent string, we can bypass this restrictions.
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

      # Extracts the product name data
      name = product.text.strip() if data else "Name Not Found"

      # Extracts the product price data
      price_element = product.find_next(price_tag, class_=price_class)
      price = price_element.text.strip() if price_element else "Price Not Found"

      # Adds the data to the empty list
      products.append(
        {
          "name": name,
          "price": price,
        }
      )

    # Prints the product name and price data
    for i, product in enumerate(products, 1):
      print(f"{i}. {product['name']} - {product['price']}")

  # If not successful, show the error message
  else:
    print(f"failed to retrieve the webpage. Status Code: {response.status_code}")

# Run the function to scrape the data
if __name__ == "__main__":
    scrape_data(
        url="target URL", 
        name_tag="html name tag", 
        name_class="html name class", 
        price_tag="html price tag", 
        price_class="html price class"
    )

# Costco example
if __name__ == "__main__":
    scrape_data(
        url="https://www.costco.com/diet-nutrition.html", 
        name_tag="span", 
        name_class="description", 
        price_tag="div", 
        price_class="price"
    )
