from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when('Search for tea')
def search_product(context):
  #  context.driver.find_element(By.ID, 'search').send_keys('tea')
     context.driver.find_element(By.CSS_SELECTOR,"").click()

@when('Account button clicked')
def click_account_button(context):
    context.driver.find_element(By.XPATH,"//a[aria-label='Account, sign in']").click()
    sleep(1)
@then('Signin page shown')
def sign_in_page(context):
    context.driver.find_element(By.XPATH,"//button[@class='styles_ndsBaseButton__4Gp2_ styles_md__Lvk4a styles_fullWidth__gA46D styles_ndsButton__XOOOH styles_md__Yc3tr styles_filled___MOAP h-margin-t-x2 h-margin-b-default']").click()
    sleep(5)