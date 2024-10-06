from selenium import webdriver
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

# open the url
driver.get('https://www.target.com/')

# Click SignIn button
driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()

# Click SignIn from side navigation
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()

# wait for 3 sec
sleep(3)

# Verify SignIn page opened
expected = 'Sign into your Target account'
actual = driver.find_element(By.XPATH, "//h1/span").text
assert expected == actual, f'Expected {expected} did not match actual {actual}'

# Verify SignIn button is shown
driver.find_element(By.ID, 'login')

# Close browser
driver.quit()