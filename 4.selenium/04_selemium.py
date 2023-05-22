from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

web = "https://www.audible.ca/search"
service = Service(
    '/Users/itsyuimoriispace/Downloads/chromedriver_mac64/chromedriver')
# define 'driver' variable
driver = webdriver.Chrome(service=service)
driver.get(web)
driver.maximize_window()


container = driver.find_element(By.CLASS_NAME, "adbl-impression-container ")
products = container.find_element('xpath', './li')
