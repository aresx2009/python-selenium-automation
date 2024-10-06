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
driver.get('https://www.amazon.com/')

# #Locate element:
# driver.find_element()# By. / value
#Locate by ID:
driver.find_element(By.ID, 'nav-logo-sprites')
#Locate by Xpath
driver.find_element(By.ID, '[input#twotabsearchtextbox.nav-input.nav-progressive-attribute]')

# Amazon logo
driver.find_element(By.ID, 'nav-logo-sprites')
# Email field
driver.find_element(By.ID, 'ap_email_login')
# Continue button
driver.find_element(By.ID, 'nav-logo-sprites')
# Conditions of use link
driver.find_element(By.ID, 'nav-logo-sprites')
# Privacy Notice link
driver.find_element(By.ID, 'nav-logo-sprites')
# Need help link
driver.find_element(By.ID, 'nav-logo-sprites')
# Forgot your password link
driver.find_element(By.ID, 'nav-logo-sprites')
# Other issues with Sign-In link
driver.find_element(By.ID, 'nav-logo-sprites')
# Create your Amazon account button
driver.find_element(By.ID, 'nav-logo-sprites')
