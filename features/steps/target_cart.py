from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when("user adds a product to cart")
def add_product(context):
    search_box = context.driver.find_element(By.ID, "search")
    search_box.send_keys("water bottle")
    search_box.submit()
    sleep(3)

    first_product_to_cart = context.driver.find_element(
        By.XPATH, "//button[contains(@id, 'addToCartButton')]"[0]
    )
    first_product_to_cart.click()
    sleep(3)

    shipping_option = context.driver.find_element(By.XPATH, "//button[@data-test='fulfillment-cell-shipping']")
    shipping_option.click()
    sleep(3)

    add_to_cart_button = context.driver.find_element(By.XPATH, "//button[@data-test='shippingButton')]")
    add_to_cart_button.click()
    sleep(3)


@then('cart contains at least one item')
def verify_cart(context):
    cart_icon = context.driver.find_element(By.XPATH, "//a[@href='/cart']")
    cart_icon.click()
    sleep(3)

    cart_items = context.driver.find_elements(
        By.XPATH, "//div[@data-test='cartItem']"
    )
    assert len(cart_items) > 0
