from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    URL = "https://www.saucedemo.com"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.ID, "user-name")
            )
        ).send_keys(username)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.ID, "password")
            )
        ).send_keys(password)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, "login-button")
            )
        ).click()

    def get_error_message(self):
        return self.driver.find_element(
            By.CSS_SELECTOR,
            "h3[data-test='error']"
        ).text

    def open_menu(self):

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, "react-burger-menu-btn")
            )
        ).click()

    def logout(self):

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, "logout_sidebar_link")
            )
        ).click()