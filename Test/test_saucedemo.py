# Test code to automate all the pages function and test them

# Importing OS module to work with file paths 
import os
# Importing sys module to manipulate the Python path
import sys
# Importing pytest for writing and executing test cases
import pytest

# Appending the parent directory to system path for module resolution
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importing LoginPage class from the pages package
from Pages.login_page import LoginPage
# Importing DashboardPage class for dashboard-related actions
from Pages.dashboard_page import DashboardPage
# Importing test data like usernames and expected outcomes
from TestData.data import Data
# Importing the environment setup fixture for browser configuration
from environment_setup import setup

# Smoke test to verify if home URL is accessible
@pytest.mark.smoke  
def test_home_url_accessibility(setup):
    # Expected homepage URL
    expected_url = "https://www.saucedemo.com/"
    # Validate if current URL matches expected
    assert expected_url == setup.current_url
    # Print success message
    print("PASS : URL TEST")

# Sanity test using multiple usernames to validate login functionality
@pytest.mark.sanity
@pytest.mark.parametrize("username,expected_result",Data.login_test_users)
def test_predefined_login(setup,username,expected_result) :
    # Initialize login page
    login = LoginPage(setup)
    # Perform login
    login.login(username, "secret_sauce")
    # Assert success or failure based on expected result
    if expected_result:
        assert login.is_login_successful(), f"Login failed for valid user: {username}"
        print(f"PASS: {username}")
    else:
        assert login.is_login_failed(), f"Expected failure for user: {username}"
        print(f" FAIL (expected): {username}")
    # Final test print
    print("PASS : PREDEFINED LOGOIN TEST")

# Smoke test to verify login fails with invalid credentials
@pytest.mark.smoke
@pytest.mark.parametrize("username, password, expected_result", [
    ("standard_user123", "secret_sauce", False),  # invalid credentials
])
def test_invalid_credential(setup, username, password, expected_result):
    # Initialize login page
    login = LoginPage(setup)
    # Attempt login with invalid credentials
    login.login(username, password)
    # Check if login behaves as expected
    if expected_result:
        assert login.is_login_successful(), f"Login failed for valid user: {username}"
        print(f"PASS: {username}")
    else:
        assert login.is_login_failed(), f"Expected failure for user: {username}"
        print(f"FAIL (expected): {username}")
    # Final test print
    print("PASS : INVALID LOGIN TEST")

# Smoke test to verify logout functionality
@pytest.mark.smoke  
def test_logout(setup) :
    # Login first
    login = LoginPage(setup)
    login.login("standard_user", "secret_sauce")
    # Perform logout
    dashboard = DashboardPage(setup)
    dashboard.logout()
    # Check if redirected to home page
    assert "saucedemo" in setup.current_url
    # Final test print
    print("PASS : LOGOUT TEST")

# Smoke test to verify clicking on cart icon
@pytest.mark.smoke  
def test_cart_icon(setup) :
    # Login first
    login = LoginPage(setup)
    login.login("standard_user", "secret_sauce")
    # Click cart icon
    dashboard = DashboardPage(setup)
    dashboard.cart_icon()
    # Verify redirection to cart
    assert "cart" in setup.current_url

# Smoke test to verify product names and prices on dashboard
@pytest.mark.smoke   
def test_product_name_price(setup) :
    # Login first
    login = LoginPage(setup)
    login.login("standard_user", "secret_sauce")
    # Validate product list
    dashboard = DashboardPage(setup)
    assert dashboard.product_verification()
    # Final test print
    print("PASS : PRODUCT NAME AND PRICES TEST")

# Functional test to validate items added to cart are displayed
@pytest.mark.functional
def test_product_in_cart(setup):
    # Login first
    login = LoginPage(setup)
    login.login("standard_user", "secret_sauce")
    # Add products and capture result
    dashboard = DashboardPage(setup)
    added_products = dashboard.add_product_to_cart()
    # Check if products were added
    assert added_products != []
    # Final test print
    print("PASS : PRODUCT LISTED IN CART TEST")

# Functional test to match cart product details with added ones
@pytest.mark.functional
def test_product_details_in_cart(setup):
    # Login first
    login = LoginPage(setup)
    login.login("standard_user", "secret_sauce")
    # Add products to cart
    dashboard = DashboardPage(setup)
    expected_products = dashboard.add_product_to_cart()  
    # Validate products in cart
    actual_products = dashboard.validate_cart_products()
    # Match added vs cart product data
    assert sorted(expected_products) == sorted(actual_products)
    # Final test print
    print("PASS : PRODUCT DETAILS VALIDATION IN CART TEST")

# Functional test to validate complete checkout flow
@pytest.mark.functional
def test_checkout_and_order_confirmation(setup):
    # Login first
    login = LoginPage(setup)
    login.login("standard_user", "secret_sauce")
    # Add products to cart
    dashboard = DashboardPage(setup)
    dashboard.add_product_to_cart()  
    # Complete the checkout
    success = dashboard.complete_checkout()
    # Verify confirmation
    assert success
    # Final test print
    print("PASS : ORDER COMPLETED AND SUCCESSFUL TEST")

# Sanity test to validate sorting options from dropdown
@pytest.mark.sanity
@pytest.mark.parametrize("option", [
    "Name (A to Z)", "Name (Z to A)",
    "Price (low to high)", "Price (high to low)"
])
def test_sorting_functionality(setup, option):
    # Perform login
    LoginPage(setup).login("standard_user", "secret_sauce")
    # Validate sorting based on option
    assert DashboardPage(setup).validate_sorting(option)
    # Final test print
    print(f"PASS: Sorting works for {option}")

# Sanity test to validate cart reset functionality
@pytest.mark.sanity
def test_reset_cart(setup) :
    # Perform login
    login = LoginPage(setup)
    login.login("standard_user", "secret_sauce")
    # Add items and reset cart
    dashboard = DashboardPage(setup)
    dashboard.add_product_to_cart() 
    assert dashboard.reset_cart() 
    # Final test print
    print("PASS : RESET CART TEST")
