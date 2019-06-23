import time
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LINKEDIN_USERNAME = os.getenv('LINKEDIN_USERNAME');
LINKEDIN_PASSWORD = os.getenv('LINKEDIN_PASSWORD');

PAUSE_TIME = 1.0

chromedriver = "/usr/local/bin/chromedriver"

driver = webdriver.Chrome()
driver.get("http://www.linkedin.com/login");

# find an element using XPath
username = driver.find_element_by_id("username")
username.send_keys(LINKEDIN_USERNAME)
password = driver.find_element_by_id("password")
password.send_keys(LINKEDIN_PASSWORD)

password.send_keys(Keys.RETURN)

wait = WebDriverWait(driver, 10)
wait.until(EC.url_matches("https://www.linkedin.com/feed"))

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
