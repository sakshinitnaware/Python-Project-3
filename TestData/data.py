class Data:

    # List of test users and expected login results
    login_test_users = [
        ("standard_user", True),
        ("locked_out_user", False),
        ("problem_user", True),
        ("performance_glitch_user", True),
        ("error_user", True),
        ("visual_user", True),
    ]

    # List of product names and their prices 
    expected_product_data = [
    ("Sauce Labs Backpack", "$29.99"),
    ("Sauce Labs Bike Light", "$9.99"),
    ("Sauce Labs Bolt T-Shirt", "$15.99"),
    ("Sauce Labs Fleece Jacket", "$49.99"),
    ("Sauce Labs Onesie", "$7.99"),
    ("Test.allTheThings() T-Shirt (Red)", "$15.99")
]
    
       