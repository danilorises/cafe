from operator import truediv
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_login_ok():
    # Open the App
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.saucedemo.com/')

    # Get username and password from page
    username = driver.find_element(By.ID,'login_credentials').text.split('\n')[1]
    password = driver.find_element(By.CLASS_NAME,'login_password').text.split('\n')[1]

    # Fill username and password and click on Login
    driver.find_element(By.ID,'user-name').send_keys(username)
    driver.find_element(By.ID,'password').send_keys(password)
    driver.find_element(By.ID,'login-button').click()

    # Checks if App title is shown
    assert 'swag labs'.upper() in driver.find_element(By.CLASS_NAME,'app_logo').text.upper()

    # Logout
    driver.find_element(By.ID,'react-burger-menu-btn').click()
    WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.ID,'logout_sidebar_link')))
    driver.find_element(By.ID,'logout_sidebar_link').click()

    # Checks if login page is shown
    assert driver.find_element(By.ID,'login-button').is_displayed()

    # Quits the App
    driver.quit()

def test_login_wrong_credentials():
    # Open the App
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.saucedemo.com/')

    # Fill wrong credentials and click on Login
    driver.find_element(By.ID,'user-name').send_keys('asdasdasd')
    driver.find_element(By.ID,'password').send_keys('asdasdasd')
    driver.find_element(By.ID,'login-button').click()

    assert 'Epic sadface: Username and password do not match any user in this service' in driver.find_element(By.CLASS_NAME,'error-message-container').text

def test_login_empty_username():
    # Open the App
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.saucedemo.com/')

    # Get password from page
    password = driver.find_element(By.CLASS_NAME,'login_password').text.split('\n')[1]

    # Fill username and password and click on Login
    driver.find_element(By.ID,'password').send_keys(password)
    driver.find_element(By.ID,'login-button').click()

    assert 'Epic sadface: Username is required' in driver.find_element(By.CLASS_NAME,'error-message-container').text

def test_login_empty_password():
    # Open the App
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.saucedemo.com/')

    # Get username from page
    username = driver.find_element(By.ID,'login_credentials').text.split('\n')[1]

    # Fill username and click on Login
    driver.find_element(By.ID,'user-name').send_keys(username)
    driver.find_element(By.ID,'login-button').click()

    assert 'Epic sadface: Password is required' in driver.find_element(By.CLASS_NAME,'error-message-container').text

def test_login_blocked_user():
    # Open the App
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.saucedemo.com/')

    # Get username and password from page
    username = driver.find_element(By.ID,'login_credentials').text.split('\n')[2]
    password = driver.find_element(By.CLASS_NAME,'login_password').text.split('\n')[1]

    # Fill username and password and click on Login
    driver.find_element(By.ID,'user-name').send_keys(username)
    driver.find_element(By.ID,'password').send_keys(password)
    driver.find_element(By.ID,'login-button').click()

    assert 'Epic sadface: Sorry, this user has been locked out.' in driver.find_element(By.CLASS_NAME,'error-message-container').text