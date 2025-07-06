class Locators:
    # ID of the username input field on the login page
    USERNAME_FIELD =  "user-name"

    # ID of the password input field on the login page
    PASSWORD_FIELD = "password"

    # ID of the login button
    LOGIN_BUTTON = "login-button"

    # XPath of the error message shown when login fails
    ERROR_MESSAGE = "//h3[@data-test='error']"

    # Dictionary to locate the inventory list using class name
    INVENTORY_LIST_LOCATOR = {
        # Locator strategy: by class name
        "by": "class name",
        # Class name value to find inventory list container
        "value": "inventory_list"
    }

    # XPath of the hamburger (side menu) button
    HAM_MENU = "//button[text()='Open Menu']"

    # XPath of the logout option in the side menu
    LOGOUT_BUTTON = "//a[text()='Logout']"

    # XPath of the shopping cart button
    CART_BUTTON = "//a[@class='shopping_cart_link']"

    # Class name used for product name elements
    PRODUCT_NAMES = "inventory_item_name"

    # Class name used for product price elements
    PRODUCT_PRICE = "inventory_item_price"

    # Class name used for all product card containers
    PRODUCT_CARDS = "inventory_item"

    # XPath of the cart badge showing number of items
    CART_BADGE = "//span[@class='shopping_cart_badge']"

    # XPath of all 'Add to cart' buttons on the products page
    ADD_CART = "//*[text() = 'Add to cart']"

    # XPath used to verify the total number of products in cart or on page
    TOTAL_PRODUCTS = "//span[text() = '4']"

    # (Duplicate) XPath of the shopping cart button
    CART_BUTTON = "//a[@class = 'shopping_cart_link']"

    # ID of the checkout button on the cart page
    CHECKOUT_BUTTON = "checkout"

    # ID of the first name input field on checkout info page
    FIRST_NAME_INPUT = "first-name"

    # ID of the last name input field on checkout info page
    LAST_NAME_INPUT = "last-name"

    # ID of the postal code input field during checkout
    POSTAL_CODE = "postal-code"

    # ID of the continue button during the checkout process
    CONTINUE_BUTTON = "continue"

    # ID of the finish button on the final checkout page
    FINISH_BUTTON = "finish"

    # ID of the continue shopping button on the cart or order complete page
    CONTINUE_SHOPPING_BUTTON = "continue-shopping"

    # ID of the sort dropdown on the products listing page
    SORT_DROPDOWN = "product_sort_container"

    # ID of the reset app state option in the side menu
    RESET_CART = "reset_sidebar_link"
