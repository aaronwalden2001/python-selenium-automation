from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, then

@given('Open Target Circle')
def open_circle(context):
    context.driver.get("https://www.target.com/circle")

    # Wait until the page heading loads
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//h2[contains(text(),'Unlock added value')]")
        )
    )


@then('user sees 2 story cards under Unlock added value')
def verify_story_cards(context):
    wait = WebDriverWait(context.driver, 10)

    # Find story cards under the section
    cards = wait.until(
        EC.presence_of_all_elements_located(
            (By.XPATH,
             "//h2[contains(text(),'Unlock added value')]/ancestor::section//a")
        )
    )

    assert len(cards) == 2
