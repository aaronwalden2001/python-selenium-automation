from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')


@given('Open Target Circle')
def open_circle(context):
    context.driver.get("https://www.target.com/circle")
    sleep(4)


@then('user sees 2 story cards under Unlock added value')
def verify_story_cards(context):
    cards = context.driver.find_elements(By.XPATH,"//div[@class='sc-422a9f7e-0 cPlFML']")
    assert len(cards) == 2
