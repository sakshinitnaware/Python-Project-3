# Dashboard code to perform add to cart, checkout the cart, sort products, reset the cart and logout
 
# Import By for locating elements using XPATH, ID, etc.
from selenium.webdriver.common.by import By
# Import Select for handling dropdown menus
from selenium.webdriver.support.ui import Select
# Import WebDriverWait to implement explicit waits
from selenium.webdriver.support.ui import WebDriverWait
# Import expected conditions to wait for element visibility, clickability, etc.
from selenium.webdriver.support import expected_conditions as EC
# Import Selenium exceptions for robust error handling
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
# Import Keys to simulate keyboard actions like ARROW_DOWN or ENTER
from selenium.webdriver.common.keys import Keys
# Import sleep to introduce hard waits (useful in some dynamic UIs)
from time import sleep
# Import Locators class where all XPATHs are defined
from Locators.locators import Locators
# Importing test data used in validation
from TestData.data import Data

# DashboardPage class for all dashboard interactions
class DashboardPage:
    # Initialize with driver and wait object
    def __init__(self, driver) :
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Function to log out user
    def logout(self) :
        print("logout funtionality")
        try :
            # Click hamburger menu
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.HAM_MENU))).click()
            # Click Logout button
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.LOGOUT_BUTTON))).click()
            print("loged out")
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException, Exception) as e :
            # Print error if logout fails
            print("cant asseign leave", e)

    # Function to check cart icon and click it
    def cart_icon(self) :
        print("cart icon visibility")
        try :
            # Validate visibility of cart icon
            cart_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators.CART_BUTTON)))
            # Click cart icon
            cart_button.click()
            sleep(5)
            print("Cart icon clicked")
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException, Exception) as e :
            print("cant asseign leave", e)

    # Function to verify product names and prices on dashboard
    def product_verification(self) :
        print("product name and price validation of dashboard")
        try :
            product_name_elements = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, Locators.PRODUCT_NAMES)))
            product_price_elements = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,Locators.PRODUCT_PRICE)))
            actual_product_names_prices = [(name.text, price.text)
                                            for name, price in zip(product_name_elements, product_price_elements)]
            if actual_product_names_prices == Data.expected_product_data :
                print("product names and prices valid")
                return True
            else :
                print("product names and prices invalid")
                return False
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException, Exception) as e :
            print("product names and prices invalid", e)
            return False

    # Function to add products to cart
    def add_product_to_cart(self):
        print("Adding items to cart")
        try:
            selected_product_data = []
            # Find all product cards
            product_cards = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, Locators.PRODUCT_CARDS)))
            print(f"Found {len(product_cards)} product cards")
            # Iterate over first 4 products
            for i, card in enumerate(product_cards[:4]):
                try:
                    # Extract name and price
                    name = card.find_element(By.CLASS_NAME, Locators.PRODUCT_NAMES).text
                    price = card.find_element(By.CLASS_NAME, Locators.PRODUCT_PRICE).text
                    button = card.find_element(By.TAG_NAME, "button")
                    # Click 'Add to Cart' button
                    button.click()
                    selected_product_data.append((name, price))
                    print(f"Added Product {i + 1}: {name} - {price}")
                    sleep(0.5)
                except Exception as inner_e:
                    print(f"Could not add product {i+1}: {inner_e}")
            # Wait for cart badge to appear
            cart_count = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators.CART_BADGE)))
            print(f"Cart badge shows: {cart_count.text} items")
            # Click on cart icon
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.CART_BUTTON))).click()
            print("Opened cart page")
            return selected_product_data
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException, Exception) as e :
            print("Error in add_product_to_cart:", e)
            return []

    # Function to validate product names and prices in cart
    def validate_cart_products(self):
        try:
            # Get product names & prices inside cart page
            cart_names = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, Locators.PRODUCT_NAMES)))
            cart_prices = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, Locators.PRODUCT_PRICE)))
            cart_data = [(n.text, p.text) for n, p in zip(cart_names, cart_prices)]
            print("Cart data:", cart_data)
            return cart_data
        except Exception as e:
            print("Failed to read cart product details:", e)
            return []

    # Function to complete the checkout process
    def complete_checkout(self):
        try:
            print("checkout functionality")
            # Click Checkout button
            self.wait.until(EC.element_to_be_clickable((By.ID,Locators.CHECKOUT_BUTTON))).click()
            print("checkout button clicked")
            # Fill in user details
            self.wait.until(EC.presence_of_element_located((By.ID,Locators.FIRST_NAME_INPUT))).send_keys("Joe")
            self.wait.until(EC.presence_of_element_located((By.ID,Locators.LAST_NAME_INPUT ))).send_keys("walker")
            self.wait.until(EC.presence_of_element_located((By.ID,Locators.POSTAL_CODE ))).send_keys("335125")
            print("details entered")
            # Click Continue button
            self.wait.until(EC.element_to_be_clickable((By.ID,Locators.CONTINUE_BUTTON))).click()
            print("continue button clicked")
            sleep(5)
            # Take screenshot of summary
            self.driver.save_screenshot("Reports/order_summary.png")
            print("Screenshot of order summary captured.")
            # Click Finish button
            self.wait.until(EC.element_to_be_clickable((By.ID,Locators.FINISH_BUTTON))).click()
            sleep(5)
            # Verify confirmation message
            confirmation = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
            return confirmation.text == "Thank you for your order!"
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException, Exception) as e :
            print("Checkout failed:", e)
            return False

    # Function to validate sorting dropdown
    def validate_sorting(self, option):
        try:
            # Select the sort dropdown
            sort = Select(self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, Locators.SORT_DROPDOWN))))
            sort.select_by_visible_text(option)
            sleep(2)
            # Get product names and prices after sort
            names = [e.text for e in self.driver.find_elements(By.CLASS_NAME, Locators.PRODUCT_NAMES)]
            prices = [float(e.text.strip("$")) for e in self.driver.find_elements(By.CLASS_NAME, Locators.PRODUCT_PRICE)]
            # Compare sorted values based on option
            if "Name" in option:
                return names == sorted(names, reverse="Z to A" in option)
            if "Price" in option:
                return prices == sorted(prices, reverse="high to low" in option)
            return False
        except Exception as e:
            print("Sort validation error:", e)
            return False

    # Function to reset the cart
    def reset_cart(self) :
        print("reset cart functinality")
        try:
            # Click 'Continue Shopping'
            self.wait.until(EC.element_to_be_clickable((By.ID,Locators.CONTINUE_SHOPPING_BUTTON))).click()
            print("continue button clicked")
            sleep(5)
            # Check if navigated to inventory page
            if "inventory" in self.driver.current_url :
                print("at dashboard")
                sleep(4)
                # Click hamburger menu
                self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators.HAM_MENU))).click()
                print("ham mnu clicked")
                # Click Reset App State
                self.wait.until(EC.element_to_be_clickable((By.ID,Locators.RESET_CART))).click()
                # Wait until cart badge disappears
                self.wait.until(EC.invisibility_of_element_located((By.XPATH, Locators.CART_BADGE)))
                print("cart is reset")
                return True
            else :
                return False
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException, Exception) as e :
            print("reset cart failed:", e)
            return False
