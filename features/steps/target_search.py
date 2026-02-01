from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from pages.main_page import MainPage
from pages.cart_page import CartPage
from time import sleep

@given('Open Target main page')
def step_open_home(context):
    context.home_page = MainPage(context.driver)
    context.main_page.open()


@when('Search for tea')
def search_product(context):
  product = context.driver.find_element(By.ID, 'search').send_keys('tea')
  product.submit()
  # sleep(5)

@then('Search results for tea are shown')
def search_results(context):
    results = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@data-test='product-grid']//li")
        )
    )
    assert len(results) > 0

@when('Account button clicked')
def click_account_button(context):
    account_btn = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@aria-label='Account, sign in']")
        )
    )
    account_btn.click()

@then('Signin page shown')
def sign_in_page(context):
    sign_in_btn = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@class='styles_ndsBaseButton__4Gp2_ styles_md__Lvk4a styles_fullWidth__gA46D styles_ndsButton__XOOOH styles_md__Yc3tr styles_filled___MOAP h-margin-t-x2 h-margin-b-default']")
        )
    )
    sign_in_btn.click()

#Cart functionality
@when('user clicks on cart icon')
def cart_click_icon(context):
    context.main_page.click_cart()

@then('user sees cart empty message')
def cart_empty_message(context):
    empty_text = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//h1[contains(text(),'Your cart is empty')]")
        )
    )
    assert empty_text.is_displayed()

#logged out
@when('user clicks Sign In button')
def click_sign_in(context):
    context.driver.find_element(By.ID,'account-sign-in').click()
    sleep(3)

@when('user clicks Sign In from side navigation')
def second_sign_in_sidemenu(context):
    context.driver.find_element(By.XPATH, "//button[@class = 'styles_ndsBaseButton__4Gp2_ styles_md__Lvk4a styles_fullWidth__gA46D styles_ndsButton__XOOOH styles_md__Yc3tr styles_filled___MOAP h-margin-t-x2 h-margin-b-default']").click()
    sleep(3)

@then('Sign In form is displayed')
def sign_in_form(context):
    context.driver.find_element(By.XPATH, "//div[@class = 'sc-e288a325-2 cwgIAc'")

#Search with variable

@when('user searches for "{product}"')
def search_product(context, product):
    search_box = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'search'))
    )
    search_box.send_keys(product)
    search_box.submit()


@then('search results are displayed')
def search_results(context):
    items = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@data-test='product-grid']//li")
        )
    )
    assert len(items) > 0