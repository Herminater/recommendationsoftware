from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

def get_ingredient_lists(url):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless") # Run in headless mode (no GUI)

    # Create a WebDriver instance using webdriver_manager
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    recipe_dict = {}

    try:
        # Navigate to the URL
        driver.get(url)

        # Get the page source after the dynamic content has loaded
        page_source = driver.page_source

        # Parse the HTML content of the page
        soup = BeautifulSoup(page_source, 'html.parser')

        # find recipes and follow links for each recipe
        recipes = soup.find('div', class_="grid grid-cols-2 gap-10 md:grid-cols-4 md:gap-15 px-5 md:px-0")
        for article in recipes.find_all('article'):
            follow_link = article.find('div', class_='relative').find('a')

            driver.get(follow_link['href'])

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'meta[itemprop="recipeIngredient"]')))

            follow_link_source = driver.page_source
            follow_link_soup = BeautifulSoup(follow_link_source, 'html.parser')

            ingredient_elements = follow_link_soup.find_all('meta', itemprop='recipeIngredient')

            if ingredient_elements:
                print("Recipe found")
                # Split and process recipe name from url
                recipe_name = follow_link['href'].split("/")[-1].replace("-", " ").capitalize()
                ingrediens_liste = []
                # Get ingrediens and add to list and add to dict with title and url
                for i, ingredient_element in enumerate(ingredient_elements):
                    ingredient = ingredient_element.get('content').replace("  ", " ").strip()
                    
                    ingrediens_liste.append(ingredient)
                   
                    recipe_dict[recipe_name] = [ingrediens_liste, follow_link['href']]

                
            else:
                print("No ingredients found. Check HTML structure.")

        return recipe_dict


    finally:
        # Close the WebDriver
        driver.quit()

# URL of the website
url = 'https://spisbedre.dk/temaer/vegetariske-gryderetter'

# Call the function with the provided URL
get_ingredient_lists(url)
