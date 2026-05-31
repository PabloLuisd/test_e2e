from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        self.driver.find_element(
            By.ID,
            "checkout"
        ).click()

#send keys: simula digitação do usuario
    def fill_information(self, first_name, last_name, postal_code):
        self.driver.find_element(
            By.ID,
            "first-name"
        ).send_keys(first_name)

        self.driver.find_element(
            By.ID,
            "last-name"
        ).send_keys(last_name)

        self.driver.find_element(
            By.ID,
            "postal-code"
        ).send_keys(postal_code)

    def continue_checkout(self):
        self.driver.find_element(
            By.ID,
            "continue"
        ).click()

    def finish_checkout(self):
        self.driver.find_element(
            By.ID,
            "finish"
        ).click()

    def get_success_message(self):
        return self.driver.find_element(
            By.CLASS_NAME,
            "complete-header"
        ).text

    def get_error_message(self):
        return self.driver.find_element(
            By.CSS_SELECTOR,
            "h3[data-test='error']"
        ).text