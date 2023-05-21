from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = '/Users/itsyuimoriispace/Downloads/chromedriver_mac64/chromedriver'
# Create a Service object using the ChromeDriverManager
s = Service(ChromeDriverManager().install())

# Create a WebDriver instance
driver = webdriver.Chrome(service=s)

# Rest of your code...

driver.get(website)


driver.quit()