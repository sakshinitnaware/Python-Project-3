# SauceDemo Online Shopping Application - Automation Testing Framework


## Project Objective

**This project focuses on automating the testing of a demo e-commerce web application to ensure reliable performance of key features such as login, 
product selection, cart operations, and checkout. The framework replicates real-time user behavior across various user roles, navigating the product 
catalog, managing cart actions, and completing purchases. Test scenarios are crafted to validate dynamic UI content, product data accuracy, and proper 
system responses. It also includes randomized interactions with products to mimic diverse customer journeys. Comprehensive and readable reports are
generated post-execution to support result analysis, ensuring functional integrity and an optimal user experience across all flows.**

## Scope
**The automation is designed to perform cross-browser validation across commonly used web browsers (e.g., Chrome, Firefox, Edge, Safari). 
The system will interact with the web elements and execute test cases covering both positive and negative scenario essential for the website**

## 🔧 Tech Stack
- Selenium
- Pytest
- Page Object Model (POM)
- Python

## 📁 Folder Structure
```
Project-3/

├── locators/
│   └── locators.py
├── pages/
│   ├── login_page.py
│   └── dashboard_page.py
├── Reports/
│   ├── saucedemo_report1.html
│   ├── saucedemo_report2.html
│   └── saucedemo_report3.html
├── testdata/
    └── data.py
├── tests/
│   └── test_saucedemo.py
└── environment_setup.py

```

- pages/: Page classes for modular automation
- locators/: Centralized locator storage
- reports/: Storing the results
- data/: Test data
- tests/: Test cases


## 🔩 Features
- Cross-browser compatible (with browser driver setup)
- Positive and negative login test cases
- UI element verification for dashboard and login
- details of product, cart details, cart checkout
- Page redirection, cart reset and logout testing

## Test Case Discription

```

| **Test Name**                    | **Description**                                                             |
| -------------------------------- | --------------------------------------------------------------------------- |
| Home URL Accessibility           | Verify if the homepage loads with the correct URL.                          |
| Valid Login                      | Log in with correct credentials and check if redirected to dashboard.       |
| Invalid Login                    | Log in with incorrect credentials and expect an error message.              |
| Logout Functionality             | Ensure the user can successfully log out.                                   |
| Cart Icon Visibility             | Verify the cart icon is visible and clickable.                              |
| Product Name & Price Check       | Check if all product names and prices are displayed correctly on dashboard. |
| Add Product to Cart              | Add items to cart and verify they are added correctly.                      |
| Validate Product Details in Cart | Ensure product names and prices in cart match selected items.               |
| Checkout & Order Confirmation    | Complete the purchase and verify the confirmation message is displayed.     |
| Sorting Functionality            | Test product sorting by name and price from the dropdown.                   |
| Reset Cart                       | Reset cart items using hamburger menu and verify cart is emptied.           |

```

## How to run 
To execute the automated test suite and generate reports, follow the steps below:

1. **Install dependencies** (if not already installed): pip install <module names> eg : selenium, pytest
2. **Run all test cases and generate a full HTML report** : pytest Test/testsaucedemo.py -d -s --html=Reports/report.html
   If the test cases have inconsistent fails and errors you can try with the below steps to avoid hassel 
          **Run all test cases and generate a full report**: pytest Test/testsaucedemo.py::<individual test name> -v -s --html=Reports/report.html
                                                   **OR**    pytest TestScript/testscript.py::<individual test name> -v -s --json-report --html=Reports/report.html
         

