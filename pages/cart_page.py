from selenium.webdriver.common.by import By

class CartPage:
        
    URL = "https://www.saucedemo.com/cart.html"

    def __init__(self, driver):
        self.driver = driver

    def remove_backpack(self):
        self.driver.find_element(
            By.ID,
            "remove-sauce-labs-backpack"
        ).click()

    def product_exists(self):
        return len(
            self.driver.find_elements(
                By.CLASS_NAME,
                "inventory_item_name"
            )
        ) > 0
    
    def cart_is_empty(self):
        return len(
            self.driver.find_elements(
                By.CLASS_NAME,
                "inventory_item_name"
            )
        ) == 0
    
    def start_checkout(self):
        self.driver.find_element(
            By.ID,
            "checkout"
        ).click()