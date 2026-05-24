from selenium.webdriver.common.by import By

class LoginPage:

    URL = "https://www.saucedemo.com"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def get_error_message(self):
        return self.driver.find_element(
            By.CSS_SELECTOR,
            "h3[data-test='error']"
        ).text

    def open_menu(self):
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()

    def logout(self):
        self.driver.find_element(By.ID, "logout_sidebar_link").click()