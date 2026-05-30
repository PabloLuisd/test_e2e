import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def driver():
    options = Options()

    options.binary_location = "/snap/firefox/8247/usr/lib/firefox/firefox"

    driver = webdriver.Firefox(options=options)

    yield driver

    driver.quit()