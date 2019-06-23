from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = "/usr/local/bin/chromedriver"

driver = webdriver.Chrome()
driver.get("https://www.mauritiusjobs.mu/jobsearch");

input = driver.find_element_by_name("search_by_keyword")
input.send_keys("developer")
input.send_keys(Keys.RETURN)

result = driver.find_element_by_xpath("//img[contains(@id, 'view_job')]")
result.click()



