from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):

    EMPTY_CART_MESSAGE = (
        By.XPATH, "//h1[contains(text(),'Your cart is empty')]"
    )

    def is_cart_empty_message_displayed(self):
        return self.wait_for_element(self.EMPTY_CART_MESSAGE).is_displayed()
