from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when('Search for tea')
def search_product(context):
  context.driver.find_element(By.ID, 'search').send_keys('tea')
  sleep(5)

@then('Search results for tea are shown')
def search_results(context):
    context.driver.find_element(By.XPATH, "//button[@aria-label = 'search']").click()
    sleep(5)

@when('Account button clicked')
def click_account_button(context):
    context.driver.find_element(By.XPATH,"//a[aria-label='Account, sign in']").click()
    sleep(5)
@then('Signin page shown')
def sign_in_page(context):
    context.driver.find_element(By.XPATH,"//button[@class='styles_ndsBaseButton__4Gp2_ styles_md__Lvk4a styles_fullWidth__gA46D styles_ndsButton__XOOOH styles_md__Yc3tr styles_filled___MOAP h-margin-t-x2 h-margin-b-default']").click()

    sleep(5)

#Cart functionality
@when('user clicks on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR,"a.styles_ndsLink__GUaai.styles_onLight__QKcK7.sc-b8685e67-1.sc-d9c75939-0.grtDbE.bgAxjv").click()
    sleep(5)

@then('user sees cart empty message')
def cart_empty_message(context):
    context.driver.find_element(By.XPATH, "//h1[@class= 'styles_ndsHeading__phw6r styles_fontSize1__OL7f3 styles_x2Margin__ZKMpf']")
    sleep(5)

#logged out
@when('user clicks Sign In button')
def click_sign_in(context):
    context.driver.find_element(By.ID,'account-sign-in').click()
    sleep(5)

@when('user clicks Sign In from side navigation')
def second_sign_in_sidemenu(context):
    context.driver.find_element(By.XPATH, "//button[@class = 'styles_ndsBaseButton__4Gp2_ styles_md__Lvk4a styles_fullWidth__gA46D styles_ndsButton__XOOOH styles_md__Yc3tr styles_filled___MOAP h-margin-t-x2 h-margin-b-default']").click()
    sleep(5)

@then('Sign In form is displayed')
def sign_in_form(context):
    context.driver.find_element(By.XPATH, "//div[@class = 'sc-e288a325-2 cwgIAc'")
    sleep(5)

#Search with variable

@when('user searches for "{product}"')
def search_product(context, product):
    search_box = context.driver.find_element(By.XPATH, "//button[@aria-label='search']")
    search_box.send_keys(product)
    search_box.submit()
    sleep(3)

@then('search results are displayed')
def search_results(context):
    results = context.driver.find_elements(By.XPATH, "//div[@data-test='product-grid']")
    assert len(results) > 0