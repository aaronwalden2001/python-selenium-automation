from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):

    CART_ICON = (By.XPATH, "//a[contains(@href,'/cart')]")

    def open(self):
        self.driver.get("https://www.target.com/")

    def click_cart(self):
        self.click(self.CART_ICON)
