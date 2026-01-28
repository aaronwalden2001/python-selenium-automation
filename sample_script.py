from selenium import webdriver
#gotta import explicit wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.wait = WebDriverWait(driver, 10)

# open the url
driver.get('https://www.google.com/')

# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Table')
search_btn = driver.find_element(By.NAME, 'btnK')
#Explicit wait
driver.wait.until(EC.element_to_be_clickable(search_btn)).click()
# wait for 4 sec
sleep(4)
#Implicit Wait - wait 5secs or less for all find element(s) parameters
driver.implicitly_wait(5)

#explicit wait - wait until condition
# click search button
driver.find_element(By.NAME, 'btnK').click()

# verify search results
assert 'Table'.lower() in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
