from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pages.general
import pages.login

def start_browser(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
    elif browser == 'safari':
        driver = webdriver.Safari()
        driver.maximize_window()
    elif browser == 'headless':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        driver = webdriver.Chrome(options=chrome_options)
    else:
        raise Exception('Please select a valid browser!')
    driver.implicitly_wait(10)
    return driver

def start_app(driver):
    driver.get('https://www.saucedemo.com/')

def logout(driver):
    driver.find_element(*pages.general.button_menu).click()
    WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable(pages.general.link_logout))
    driver.find_element(*pages.general.link_logout).click()

def close_browser(driver):
    driver.quit()

def login(driver,username,password):
    driver.find_element(*pages.login.input_username).send_keys(username)
    driver.find_element(*pages.login.input_password).send_keys(password)
    driver.find_element(*pages.login.button_login).click()