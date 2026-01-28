from pages.base_page import Page

class MainPage(Page):

    def open_page(self):
        self.open_url('https://www.target.com/')
