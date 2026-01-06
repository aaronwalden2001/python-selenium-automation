from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://stackoverflow.com/users/signup')

#Header text
driver.find_element(By.XPATH, "//h1[@class='flex--item fs-headline1 fw-bold lh-xs mb8 ws-nowrap']")

# fine Print
driver.find_element(By.XPATH, "//div[@class='flex--item js-terms fs-caption fc-black-400 ta-left']")

#Email field
driver.find_element(By.XPATH,"//input[@id='email']")

# Password field
driver.find_element(By.XPATH,"//input[@id='password']")

# Display name field
driver.find_element(By.CSS_SELECTOR,"svg.ps-absolute.r8.t8.c-pointer.js-show-password.svg-icon.iconEyeOffSm")

# Sign up button
driver.find_element(By.XPATH, "//button[@id='submit-button']")

# Google sign up button
driver.find_element(By.XPATH,"//button[@class = 'flex--item s-btn s-btn__icon s-btn__google bar-md ba bc-black-225']")

# GitHub sign up button
driver.find_element(By.CSS_SELECTOR,"button.flex--item s-btn s-btn__icon s-btn__github bar-md ba bc-black-225")

# Teams signup link
driver.find_element(By.XPATH,"//a[@href = 'https://stackoverflow.com/teams?utm_source=so-owned&utm_medium=product&utm_campaign=free-50&utm_content=public-sign-up']")
