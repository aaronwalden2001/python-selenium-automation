from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then
from time import sleep

@when("user adds a product to cart")
def add_product(context):
    wait = WebDriverWait(context.driver, 10)

    # Search for product
    search_box = wait.until(
        EC.presence_of_element_located((By.ID, "search"))
    )
    search_box.send_keys("water bottle")
    search_box.submit()
    sleep(2)

    # Find all Add to Cart buttons and click the first one
    add_to_cart_buttons = context.driver.find_elements(
        By.XPATH, "//button[contains(@id,'addToCartButton')]"
    )
    add_to_cart_buttons[0].click()

    # Wait for fulfillment options
    shipping_option = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@data-test='fulfillment-cell-shipping']")
        )
    )
    shipping_option.click()

    # Wait for final Add to Cart button
    final_add_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@data-test='shippingButton']")
        )
    )
    final_add_button.click()
    sleep(2)


@then("cart contains at least one item")
def verify_cart(context):
    wait = WebDriverWait(context.driver, 10)

    cart_icon = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/cart']"))
    )
    cart_icon.click()

    # Wait for cart items to load
    cart_items = wait.until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@data-test='cartItem']")
        )
    )

    assert len(cart_items) > 0
