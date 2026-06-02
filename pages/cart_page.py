from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    URL = "https://www.saucedemo.com/cart.html"

    def __init__(self, driver):
        self.driver = driver

    def remove_backpack(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, "remove-sauce-labs-backpack")
            )
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
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, "checkout")
            )
        ).click()