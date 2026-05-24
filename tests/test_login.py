from pages.login_page import LoginPage

def test_login_valido(driver):
    #instanciando
    login_page = LoginPage(driver)
    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    assert "inventory" in driver.current_url


def test_login_invalido(driver):
    login_page = LoginPage(driver)
    login_page.open()

    login_page.login(
        "standard_user",
        "senha_errada"
    )

    error_message = login_page.get_error_message()

    assert "Username and password do not match" in error_message


def test_logout(driver):
    login_page = LoginPage(driver)
    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    login_page.open_menu()
    login_page.logout()

    assert driver.find_element(By.ID, "login-button").is_displayed()