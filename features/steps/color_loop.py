from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then


@when('user selects each available color')
def select_each_color(context):
    #original products not available
    context.driver.get("https://www.target.com/p/wranglers-men-39-s-relaxed-fit-straight-jeans-dark-wash-30x30/-/A-90919093#lnk=sametab")

    wait = WebDriverWait(context.driver, 10)

    # Wait for color options to load
    color_buttons = wait.until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//a[contains(@aria-label, 'Color')]")
        )
    )

    # Loop through each color
    for color in color_buttons:
        color_name = color.get_attribute("aria-label")

        wait.until(EC.element_to_be_clickable(color)).click()

        # Verify this color is selected
        assert color.get_attribute("aria-checked") == "true", \
            f"Color {color_name} was not selected"


@then('each selected color has been selected')
def verify_color_selection(context):
    # Verification already done in loop
    pass
