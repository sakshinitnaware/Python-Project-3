# environment code to automate the drivers and browser functions 

# Import pytest for defining setup fixtures 
import pytest

# Import Selenium WebDriver core
from selenium import webdriver

# Import Chrome driver service
from selenium.webdriver.chrome.service import Service as ChromeService
# Import Firefox driver service
from selenium.webdriver.firefox.service import Service as FirefoxService
# Import Edge driver service
from selenium.webdriver.edge.service import Service as EdgeService

# Import Chrome options for headless mode and other configs
from selenium.webdriver.chrome.options import Options as ChromeOptions
# Import Firefox options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
# Import Edge options
from selenium.webdriver.edge.options import Options as EdgeOptions

# Automatically download and manage the correct version of ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager
# Automatically download and manage the correct version of GeckoDriver (Firefox)
from webdriver_manager.firefox import GeckoDriverManager
# Automatically download and manage the correct version of EdgeDriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Pytest fixture to provide a reusable browser setup for each test function
@pytest.fixture(scope="function")         
def setup():
    # Initialize the driver as None before launching any browser
    driver = None
    try :
        # Try launching Chrome browser using WebDriverManager
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    except Exception as E1 :
        # Print Chrome launch failure message
        print("Chrome not available:", E1)
        
        try :
            # Try launching Firefox browser as fallback
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        except Exception as E2 :
            # Print Firefox launch failure message
            print("Firefox not available:", E2)

            try :
                # Try launching Edge browser as final fallback
                driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
            except Exception as E3 :
                # Print Edge launch failure message
                print("Firefox not available:", E3)    

    # Maximize the browser window (has no effect in headless, but safe to call)
    driver.maximize_window()
    # Open the SauceDemo login page
    driver.get("https://www.saucedemo.com/")
    # Yield the driver instance to the test function
    yield driver
    # Quit the driver and close the browser after the test
    driver.quit()
