## Useful Selenium commands
Start the browser
```python
driver = webdriver.Safari()
```
Set implicit wait
```python
driver.implicitly_wait(10)
```
Maximize browser window
```python
driver.maximize_window()
```
Open webpage
```python
driver.get('http://www.pudim.com.br')
```
Click an element
```python
driver.find_element(By.ID,'loginButton').click()
```
Wait for element to be interactable
```python
WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.ID,'button')))
```
Get text from element
```python
texto = driver.find_element(By.ID,'mensagem').text
```
Double-click element
```python
ActionChains(driver).double_click(driver.find_element(By.ID,'send')).perform()
```
Hover over element
```python
ActionChains(driver).move_to_element(driver.find_element(By.ID,'mousehover')).perform()
```
Right-click element
```python
ActionChains(driver).context_click(driver.find_element(By.ID,'send')).perform()
```
Drag-and-drop between elements
```python
ActionChains(driver).drag_and_drop(driver.find_element(By.ID,'objectOrigin'),driver.find_element(By.ID,'objectDestination')).perform()
```
Insert text into element
```python
driver.find_element(By.ID,'email').send_keys('danilocaires@outlook.com')
```
Erase text from element
```python
driver.find_element(By.ID,'textbox').clear()
```
Select option in dropdown
```python
Select(driver.find_element(By.ID,"dropdown-class-example")).select_by_visible_text("Option3")
```
Get a list of elements
```python
elements = driver.find_elements(By.CSS_SELECTOR,'')
```
Change focus to frame
```python
driver.switch_to.frame('frameID')
```
Change focus back out of the frame
```python
driver.switch_to.default_content()
```
Change the browser window/tab
```python
driver.switch_to.window(driver.window_handles[1])
```
Execute javascript command
```python
driver.execute_script('window.scrollBy(0,500);')
```
Take a screenshot
```python
driver.get_screenshot_as_file('screen.png')
```
Quit the browser
```python
driver.quit()
```
(imports used)
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
```

## Useful Chrome Options

```python
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument('headless')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--disable-popup-blocking')
chrome_options.add_argument('--incognito')
chrome_options.add_argument('disable-extensions')
chrome_options.add_argument('--window-size=<width>,<height>')
chrome_options.add_argument('--user-data-dir=<directory>')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=chrome_options)
```

For more chrome options visit: https://peter.sh/experiments/chromium-command-line-switches/

## Terminal Commands
Run all tests
```
pytest -vtrab_
```
Run specific marked tests
```
pytest -m marker_name
```
Run all tests and generate an HTML report
```
pytest --html='reports/results.html'
```
Create/Update requirements list to execute the project
```
pip freeze > requirements.txt
```
Restore dependencies to run the project
```
pip install -r requirements.txt
```