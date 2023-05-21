from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)



def main():
    global driver
    website = 'https://www.adamchoi.co.uk/overs/detailed'
    service = Service('/Users/itsyuimoriispace/Downloads/chromedriver_mac64/chromedriver')
    # define 'driver' variable
    driver = webdriver.Chrome(service=service)
    # open Google Chrome with chromedriver
    driver.get(website)

    # locate and click on a button
    all_matches_button = driver.find_element('xpath', '//label[@analytics-event="All matches"]')
    all_matches_button.click()

    # # select dropdown and select element inside by visible text
    # dropdown = Select(driver.find_element_by_id('country'))
    # dropdown.select_by_visible_text('Spain')
    # # implicit wait (useful in JavaScript driven websites when elements need seconds to load and avoid error "ElementNotVisibleException")
    # time.sleep(3)

#driver.quit()

if __name__ == '__main__':
    main()