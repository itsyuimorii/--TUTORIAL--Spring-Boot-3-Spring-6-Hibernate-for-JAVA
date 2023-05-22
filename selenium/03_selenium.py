from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

date = []
home_team = []
score = []
away_team = []

def main():
    global driver

    # define the website to scrape and path where the chromediver is located
    website = 'https://www.adamchoi.co.uk/overs/detailed'
    service = Service('/Users/itsyuimoriispace/Documents/GitHub/Web Scraping in Python BeautifulSoup, Selenium & Scrapy 2023/chromedriver_mac64/chromedriver')
    # define 'driver' variable
    driver = webdriver.Chrome(service=service)
    # open Google Chrome with chromedriver
    driver.get(website)
    # locate and click on a button
    all_matches_button = driver.find_element('xpath', '//label[@analytics-event="All matches"]')
    all_matches_button.click()

    elements = driver.find_elements(By.TAG_NAME, 'tr')

    for element in elements:
        date.append(element.find_element(By.XPATH, './td[1]').text)
        home_team.append(element.find_element(By.XPATH, './td[2]').text)
        score.append(element.find_element(By.XPATH, './td[3]').text)
        away_team.append(element.find_element(By.XPATH, './td[4]').text)

        # quit driver we opened at the beginning
    driver.quit()

    # Export data
    export(date, home_team, score, away_team)


def export(date, home_team, score, away_team):
    # Create Dataframe in Pandas and export to CSV (Excel)
    df = pd.DataFrame({'date': date, 'home_team': home_team, 'score': score, 'away_team': away_team})
    df.to_csv('football_data.csv', index=False)
    print(df)


if __name__ == '__main__':
    main()