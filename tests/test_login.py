import utils.general
import pages.general
import pages.login

def test_login_ok(driver):
    """Test the login fuction with correct credentials and check if the user logged in sucessfully."""
    username = driver.find_element(*pages.login.div_usernames).text.split('\n')[1]
    password = driver.find_element(*pages.login.div_passwords).text.split('\n')[1]
    utils.general.login(driver,username,password)
    assert 'swag labs'.upper() in driver.find_element(*pages.general.label_logo).text.upper()

def test_login_wrong_credentials(driver): 
    """Test the login fuction with incorrect credentials and check if the correct error message is displayed"""
    utils.general.login(driver,'asdasdasd','asdasdasd')
    assert 'Epic sadface: Username and password do not match any user in this service' in driver.find_element(*pages.login.div_error).text

def test_login_empty_username(driver):
    """Test the login fuction with empty username and check if the correct error message is displayed"""
    password = driver.find_element(*pages.login.div_passwords).text.split('\n')[1]
    utils.general.login(driver,'',password)
    assert 'Epic sadface: Username is required' in driver.find_element(*pages.login.div_error).text

def test_login_empty_password(driver):
    """Test the login fuction with empty password and check if the correct error message is displayed"""
    username = driver.find_element(*pages.login.div_usernames).text.split('\n')[1]
    utils.general.login(driver,username,'')
    assert 'Epic sadface: Password is required' in driver.find_element(*pages.login.div_error).text

def test_login_blocked_user(driver):
    """Test the login fuction with blocked credentials and check if the correct error message is displayed"""
    username = driver.find_element(*pages.login.div_usernames).text.split('\n')[2]
    password = driver.find_element(*pages.login.div_passwords).text.split('\n')[1]
    utils.general.login(driver,username,password)
    assert 'Epic sadface: Sorry, this user has been locked out.' in driver.find_element(*pages.login.div_error).text