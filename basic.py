import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# path to ChromeDriver
chromedriver = "/usr/local/bin/chromedriver"

# create an instance of Chrome Webdriver 
driver = webdriver.Chrome()

# navigate to a url
driver.get("http://www.google.com/search?q=pymug");

print(driver.title)
print(driver.current_url)

# find an element and interact with it
elem = driver.find_element_by_xpath("//div[@class='r'][1]/a")
elem.send_keys(Keys.RETURN)

# wait 5 seconds and close the browser
time.sleep(5)
driver.close()
