import pytest
from selenium import webdriver

#Criando/Abrindo/Fechando navegador
@pytest.fixture
def driver():
    driver = webdriver.Firefox()

    yield driver

    driver.quit()