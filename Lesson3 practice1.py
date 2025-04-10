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
driver.get('https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Ftag%3Damazusnavi-20%26hvadid%3D675149238949%26hvpos%3D%26hvnetw%3Dg%26hvrand%3D2377997298194505641%26hvpone%3D%26hvptwo%3D%26hvqmt%3De%26hvdev%3Dc%26hvdvcmdl%3D%26hvlocint%3D%26hvlocphy%3D9026805%26hvtargid%3Dkwd-29089120%26ref%3Dnav_signin%26hydadcr%3D15116_13597370&prevRID=Q40QYJ4JSFHCJ1GX0JX3&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

#First and last name
driver.find_element(By.ID, 'ap_customer_name')

#Mobile number or email
driver.find_element(By.ID, 'ap_email')

#Create a password
driver.find_element(By.ID, 'ap_password')

#Show password
driver.find_element(By.ID, 'auth-register-show-password-checkbox')

#Continue button
driver.find_element(By.ID, 'auth-register-show-password-checkbox')

#Conditions of Use Link
driver.find_element(By.XPATH, "//a[contains(@href, 'condition_of_use')]")

#Privacy Notice Link
driver.find_element(By.XPATH, "//a[contains(@href, 'privacy_notice')]")

#Create a free business account Link
driver.find_element(By.ID, 'ab-enhanced-registration-link')

#sign in button
driver.find_element(By.CSS_SELECTOR, '.a-icon a-accordion-radio.a-icon-radio-inactive')