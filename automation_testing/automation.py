import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option('detach', True)

# The code below automatically installs a chrome driver and assigns it to the chrome_driver variable instead of manually downloading a chrome driver online and also shows how to use it.
chrome_driver = ChromeDriverManager().install()
chrome_browser = webdriver.Chrome(service=Service(chrome_driver), options=options)

# This code below is used when you manually downloaded the chrome driver and you input its file path into the executable_path parameter
# chrome_browser = webdriver.Chrome(service=Service(executable_path='./chromedriver.exe'), options=options)


chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/python/pytest-run-webdriver-tests-in-parallel')

search_text = chrome_browser.find_element(By.ID, 'edit-search-block-form--2')
search_text.clear()
search_text.send_keys('python')
time.sleep(2)
search_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-primary')
search_button.click()
chrome_browser.quit()
