# Login code to perform login functions

# Importing the By class to locate elements using different strategies like XPATH 
from selenium.webdriver.common.by import By

# Importing WebDriverWait to apply explicit waits on web elements
from selenium.webdriver.support.ui import WebDriverWait

# Importing expected conditions to wait for elements to be visible, clickable, etc.
from selenium.webdriver.support import expected_conditions as EC

# Importing exceptions to handle various Selenium-related runtime errors
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException

# Importing sleep to pause execution temporarily
from time import sleep

# Importing the locators used for finding elements on the page
from Locators.locators import Locators

# Importing test data like usernames and passwords
from TestData.data import Data

# Importing environment setup file, probably containing fixture/configuration
import environment_setup

# Defining the LoginPage class for login-related page actions
class LoginPage :

    # Constructor to initialize the driver and wait object
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Method to perform login using username and password
    def login(self, username, password):
        self.wait.until(EC.presence_of_element_located((By.ID,Locators.USERNAME_FIELD))).send_keys(username)
        self.wait.until(EC.presence_of_element_located((By.ID,Locators.PASSWORD_FIELD))).send_keys(password)
        self.wait.until(EC.presence_of_element_located((By.ID,Locators.LOGIN_BUTTON))).click()

    # Method to check if login was successful by verifying presence of inventory list
    def is_login_successful(self):
        try:
            by = Locators.INVENTORY_LIST_LOCATOR["by"]
            value = Locators.INVENTORY_LIST_LOCATOR["value"]
            locator = (getattr(By, by.upper().replace(" ", "_")), value)
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except:
            return False

    # Method to check if login failed by checking if error message is visible
    def is_login_failed(self):
        try:
            error = self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators.ERROR_MESSAGE)))
            return error.is_displayed()
        except:
            return False
