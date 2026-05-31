from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout_valido(driver):

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.open()

    login.login(
        "standard_user",
        "secret_sauce"
    )

    inventory.add_backpack()

    inventory.open_cart()

    cart.start_checkout()

    checkout.fill_information(
        "Fulano",
        "Siclano",
        "95690000"
    )

    checkout.continue_checkout()

    checkout.finish_checkout()

    assert (
        checkout.get_success_message()
        == "Thank you for your order!"
    )

def test_checkout_invalido(driver):

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.open()

    login.login(
        "standard_user",
        "secret_sauce"
    )

    inventory.add_backpack()

    inventory.open_cart()

    cart.start_checkout()

    checkout.continue_checkout()

    assert (
        "Error"
        in checkout.get_error_message()
    )