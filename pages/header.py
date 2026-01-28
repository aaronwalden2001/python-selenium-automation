from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page

class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_ICON = (By.CSS_SELECTOR, '[data-test=@web/Search/SearchButton]')
    def search(self):
        self.input_text('tea', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_ICON)
        sleep(10)