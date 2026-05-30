from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_adicionar_produto(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    login.open()
    login.login(
        "standard_user",
        "secret_sauce"
    )

    inventory.add_backpack()
    inventory.open_cart()
    assert cart.product_exists()

def test_remover_produto(driver):

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    login.open()
    login.login(
        "standard_user",
        "secret_sauce"
    )

    inventory.add_backpack()
    inventory.open_cart()

    cart.remove_backpack()
    
    assert cart.cart_is_empty()