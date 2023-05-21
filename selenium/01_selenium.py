from selenium import webdriver
from selenium.webdriver.chrome.service import Service


website = 'https://www.adamchoi.co.uk/overs/detailed'
service = Service('/Users/itsyuimoriispace/Downloads/chromedriver_mac_arm64/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get(website)

all_matches_button = driver.find_element('xpath', '//label[@analytics-event="All matches"]')
all_matches_button.click()

driver.quit()