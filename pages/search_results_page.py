from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page

class SearchResultsPage(Page):
    SEARCH_RESULTS_TEXT = (By.XPATH, )

    def verify_search_results_text(self, text):
        actual_text = self.browser.find_element(*self.SEARCH_RESULTS_TEXT).text
        assert self.SEARCH_RESULTS_TEXT in text
