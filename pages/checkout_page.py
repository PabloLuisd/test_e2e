from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, "checkout")
            )
        ).click()

    # send_keys: simula digitação do usuário
    def fill_information(
        self,
        first_name,
        last_name,
        postal_code
    ):

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.ID, "first-name")
            )
        ).send_keys(first_name)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.ID, "last-name")
            )
        ).send_keys(last_name)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.ID, "postal-code")
            )
        ).send_keys(postal_code)

    def continue_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, "continue")
            )
        ).click()

    def finish_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, "finish")
            )
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